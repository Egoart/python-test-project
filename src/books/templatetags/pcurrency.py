from django import template
import requests

register = template.Library()

USD_ENDPOINT = 'https://www.nbrb.by/api/exrates/rates/431'

@register.simple_tag
def currency_rate():
    result = requests.get(USD_ENDPOINT)
    return result.json().get("Cur_OfficialRate")