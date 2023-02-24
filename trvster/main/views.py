from django.shortcuts import render
from rest_framework.views import APIView

import folium

def maptest(request):
    map = folium.Map(location=[35.672868, 139.767158], zoom_start=16)
    maps=map._repr_html_()

    return render(request,'../templates/main.html',{'map' : maps})