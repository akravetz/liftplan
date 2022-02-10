import os
import shutil
from pathlib import Path
from typing import Any
from jinja2 import Template

from core import models
from .output import OutputFormat, Chapter, Page

_DAY_OF_WEEK_INDEX = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def _render(template_file: str, **kwargs: Any) -> str:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_fn = f"{base_dir}/html_templates/{template_file}"
    with open(full_fn, "r", encoding="utf-8") as f_obj:
        return Template(f_obj.read()).render(kwargs)


def generate_day_table(
    day: models.Day, gen_header: bool = True, html_class: str = "exercises"
) -> str:
    # count sets per muscle group, to create header table
    exercises = day.exercises
    set_count = {name: 0 for name in models.MuscleGroup.__members__}
    exercise_count = {name: 0 for name in models.MuscleGroup.__members__}
    for es_ in exercises:
        musc_group_name = es_.exercise.muscle_group.name
        set_count[musc_group_name] += len(es_.sets)
        exercise_count[musc_group_name] += 1
        # count intensifiers as an additional set
        for set_ in es_.sets:
            if isinstance(set_.intensifier, models.Dropset):
                set_count[musc_group_name] += set_.intensifier.n_drops
            elif isinstance(set_.intensifier, models.Myorep):
                set_count[musc_group_name] += 3

    # we want to create a table that has two muscle groups per row with a
    # spacing column between them
    set_count = {k: v for k, v in set_count.items() if v > 0}
    exercise_count = {k: v for k, v in exercise_count.items() if v > 0}

    sorted_keys = sorted(
        set_count.keys(), key=lambda x: models.MuscleGroup.__members__[x]
    )
    all_exercises = [
        dict(
            muscle_group=key.title(),
            n_exercises=exercise_count[key],
            n_sets=set_count[key],
        )
        for key in sorted_keys
    ]

    total_sets = sum(set_count.values())
    total_exercises = sum(exercise_count.values())
    return _render(
        "exercise_table.html",
        day=day,
        day_of_week=_DAY_OF_WEEK_INDEX[day.day_offset],
        exercise_groups=all_exercises,
        total_exercises=total_exercises,
        total_sets=total_sets,
        gen_header=gen_header,
        html_class=html_class,
    )


def week_summary_html(block: models.Block, week_index) -> str:
    page_html = _render(
        "week_summary.html",
        block=block,
        week_index=week_index,
        generate_day_table=generate_day_table,
    )
    return page_html


def day_html(block: models.Block, week_index, day: models.Day) -> str:
    page_html = _render(
        "day.html",
        block=block,
        week_index=week_index,
        day_of_week=_DAY_OF_WEEK_INDEX[day.day_offset],
        day=day,
        generate_day_table=generate_day_table,
    )
    return page_html


class HtmlOutput(OutputFormat):
    def __init__(self, program: models.Program):
        super().__init__(program)
        self.process()

    def process(self) -> None:
        week_index = 0
        for block in self.program.blocks:
            for _ in range(block.n_weeks):
                week_index += 1
                chap = Chapter()
                summary_page = Page(
                    week_summary_html(block, week_index).encode("utf-8")
                )
                chap.add_page(summary_page)
                pages = [
                    Page(day_html(block, week_index, day).encode("utf-8"))
                    for day in block.days
                    if len(day.exercises) > 0
                ]
                chap.add_pages(pages)

                self.add_chapter(chap)

    def format_name(self) -> str:
        return "html"

    def output(self, filename: str, **kwargs) -> None:
        overwrite = kwargs.get("overwrite", False)
        base_path = Path(filename)
        base_path.mkdir(exist_ok=overwrite)
        # write the chapter output
        for chap_idx, chapter in enumerate(self.chapters):
            chapter_path = base_path.joinpath(f"chapter{chap_idx}")
            chapter_path.mkdir(exist_ok=overwrite)
            for page_idx, page in enumerate(chapter.pages):
                page_path = chapter_path.joinpath(f"page{page_idx}.html")
                with page_path.open("wb") as f_obj:
                    f_obj.write(page.content)
        # write the static files as necessary
        static_from_path = Path(__file__).parent.absolute().joinpath("html_static")
        static_to_path = base_path.joinpath("static")
        shutil.copytree(static_from_path, static_to_path, dirs_exist_ok=overwrite)
