from django.shortcuts import render
from rest_framework.views import APIView

import folium
import json

def maptest(request):
    with open('./tokyo_json/tokyogeo_ku.geojson','r') as geo:
        tokyo_geo = json.load(geo)
    map = folium.Map(location=[35.672868, 139.767158], zoom_start=10)
    folium.GeoJson(
        tokyo_geo,
        name='tokyoGeo'
    ).add_to(map)
    maps=map._repr_html_()
    return render(request,'../templates/main.html',{'map' : maps})