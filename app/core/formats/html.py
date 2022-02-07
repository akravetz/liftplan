from core import models


def generate_set_table(exercises: list[models.ExerciseProgram]) -> str:
    # count sets per muscle group, to create header table
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
                set_count[musc_group_name] += 1

    # we want to create a table that has two muscle groups per row with a
    # spacing column between them
    set_count = {k: v for k, v in set_count.items() if v > 0}
    exercise_count = {k: v for k, v in exercise_count.items() if v > 0}
    table_html = ""
    for key in sorted(
        set_count.keys(), key=lambda x: models.MuscleGroup.__members__[x]
    ):
        muscle_group = key.title()
        table_html = f"""{table_html}
            <tr>
              <td>{muscle_group}</td><td>{exercise_count[key]} exercises<td>{set_count[key]} sets</td>
            </tr>
              """
    total_sets = sum(set_count.values())
    total_exercises = sum(exercise_count.values())

    table_html = f"""{table_html}
    <tr>
      <td></td><td>{total_exercises} exercises</td><td>{total_sets} sets</td>
    </tr>"""

    return f"""<table class="table table-striped table-bordered border-primary">
      <tbody>
      {table_html}
      </tbody>
      </table>"""


def day_to_html(day: models.Day) -> str:
    offset_to_dow = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    header = f"<h3>{offset_to_dow[day.day_offset]} - {day.name} </h2>"
    table_html = generate_set_table(day.exercises)
    result = f"""<div class="row">{header}</div>
    <div class="row">
        <div class="col"></div>
        <div class="col">{table_html}</div>
        <div class="col"></div>
    </div>"""

    return result


def block_to_html(block: models.Block) -> str:
    title = f'<div class="row"><h1>{block.name} ({block.n_weeks} weeks)</div>'
    result = ""
    for day in block.days:
        day_md = day_to_html(day)
        result = f'{result}\n<div style="page-break-after: always;"></div>\n{day_md}'
    return f"{title}{result}"


def program_to_html(program: models.Program) -> str:
    result = ""
    for block in program.blocks:
        block_md = block_to_html(block)
        result = f"{result}\n{block_md}"
    return f"""
    <html lang="en">
    <head>
      <meta charset="utf-8" />
      <title>{program.name}</title>
      <meta name="viewport" content="width=device-width, initial-scale=1">
      <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    </head>
    <body>
    <div class="container">
    {result}
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
    </body>
    </html>"""
