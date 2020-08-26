from django.shortcuts import render_to_response, redirect
from django.urls import reverse

import csv
with open('data-398-2018-08-30.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)


# def index(request):
#     return redirect(reverse(bus_stations))


# def bus_stations(request):
#     current_page = 1
#     next_page_url = 'write your url'
#     return render_to_response('index.html', context={
#         'bus_stations': [{'Name': 'название', 'Street': 'улица', 'District': 'район'}],
#         'current_page': current_page,
#         'prev_page_url': None,
#         'next_page_url': next_page_url,
#     })

