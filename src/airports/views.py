from django.shortcuts import render
from django.http import HttpResponse
from .airtports_base import AIRPORTS_CODES

# Create your views here.

# AIRPORTS_CODES = {
#     'DXB': 'DUBAI',
#     'HAJ':'HANNOVER',
#     'HAN':'HANOI',
#     'LGW': 'LONDON GATWICK',
#     'LHR': 'LONDON HEATHROW',
#     'LAX': 'LOS ANGELES',
#     'ORY': 'PARIS ORLY',
#     'ROM': 'ROME',
#     'SIN': 'SINGAPORE-CHANGI',
#     'VNO': 'VILNIUS' 
# }

def airports(request, code):
    city = AIRPORTS_CODES.get(code.upper(), 'UNKNOWN')
    ctx = {
        'city': city 
    }
    return render(request, template_name='airports.html', context=ctx)

def airports_home(request):
    codes = AIRPORTS_CODES.keys()
    
    cctx = {
        'codes': codes
    }
    return render(request, template_name='index.html', context=cctx)