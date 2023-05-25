from django import template
import calendar

register = template.Library()

@register.filter
def num_days_in_month_filter(date):
    num_days = calendar.monthrange(date.year, date.month)[1]
    return range(1, num_days+1)
