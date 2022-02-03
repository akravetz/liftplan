from core.programs import PPL_V2
from core import program_to_html


def main():
    html = program_to_html(PPL_V2)
    print(html)


if __name__ == "__main__":
    main()
