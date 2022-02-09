import os.path
from typing import Any
from jinja2 import Template

from core import models
from .output import OutputFormat, Chapter, Page


def _render(template_file: str, **kwargs: Any) -> str:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    full_fn = f"{base_dir}/html_templates/{template_file}"
    with open(full_fn, "r", encoding="utf-8") as f_obj:
        return Template(f_obj.read()).render(kwargs)


def generate_day_table(day: models.Day) -> str:
    offset_to_dow = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
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
            elif isinstance(set_.intensifier, models.Dropset):
                # TODO: fix this
                set_count[musc_group_name] += 0

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
        day_of_week=offset_to_dow[day.day_offset],
        exercise_groups=all_exercises,
        total_exercises=total_exercises,
        total_sets=total_sets,
    )


def week_summary_html(block: models.Block, week_index) -> str:
    page_html = _render(
        "week_summary.html",
        block=block,
        week_index=week_index,
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
                chap.add_pages([summary_page])
                self.add_chapter(chap)

    def format_name(self) -> str:
        return "html"

    def output(self, filename: str, **kwargs) -> None:
        pass
