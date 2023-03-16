from django import template

register = template.Library()


@register.simple_tag
def date_start_end(task):
    row_start = task.start_date.month + 1
    row_end = task.due_date.month + 2

    row_start_end = {
        "row_start": row_start,
        "row_end": row_end,
    }

    return row_start_end
