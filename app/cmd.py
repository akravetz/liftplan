import os.path
import re
import glob
import argparse
from typing import Any

from jinja2 import Template

from core.programs import PPL_V2
from core.formats import HtmlOutput

HTML_OUT_DIR = "ppl_v2"
PDF_OUT_DIR = "pdf"


def _render(template_file: str, **kwargs: Any) -> str:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_fn = f"{base_dir}/gen_pdf/{template_file}"
    with open(full_fn, "r", encoding="utf-8") as f_obj:
        return Template(f_obj.read()).render(kwargs)


def html_to_pdf(base_dir, html_dir, pdf_dir):
    virtual_base = "/usr/src/app/src"
    html_abs_path = f"{base_dir}/{html_dir}"
    try:
        os.mkdir(f"{base_dir}/{pdf_dir}")
    except:
        pass
    html_files = [
        path.replace(f"{base_dir}/", f"{virtual_base}/")
        for path in glob.glob(f"{html_abs_path}/**/*.html", recursive=True)
    ]
    out_files = [out_file.replace(".html", "") for out_file in html_files]
    out_files = [
        out_file.replace(f"{virtual_base}/{html_dir}/", "") for out_file in out_files
    ]
    out_files = [re.sub(r"[^A-Za-z0-9]", "_", path) for path in out_files]
    params = [
        {
            "in_path": f"{in_path}",
            "out_path": f"{virtual_base}/{pdf_dir}/{out_file}.pdf",
        }
        for in_path, out_file in zip(html_files, out_files)
    ]

    script_content = _render("template.js", files=params)
    with open(f"{base_dir}/{pdf_dir}/script.js", "w") as f:
        f.write(script_content)


def parse_args():
    parser = argparse.ArgumentParser(description="lift generator")
    parser.add_argument(
        "--html",
        action="store_true",
        help="generate html output",
    )
    parser.add_argument(
        "--pdf",
        action="store_true",
        help="generate pdf output",
    )
    parser.add_argument(
        "--collate",
        action="store_true",
        help="generate pdf output",
    )

    return parser.parse_args()


def main():
    args = parse_args()
    common_base = "/home/akravetz/code"
    html_out_path = f"{common_base}/{HTML_OUT_DIR}"
    pdf_out_path = PDF_OUT_DIR
    if args.html:
        out = HtmlOutput(PPL_V2)
        out.output(html_out_path, overwrite=True)
    if args.pdf:
        html_to_pdf(common_base, HTML_OUT_DIR, pdf_out_path)
    if args.collate:
        pass


if __name__ == "__main__":
    main()
