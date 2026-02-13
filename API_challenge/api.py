import random
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status as http_status

SISTEMAS_AVERIADOS = {
    "navigation": "NAV-01",
    "communications": "COM-02",
    "life_support": "LIFE-03",
    "engines": "ENG-04",
    "deflector_shield": "SHLD-05"
}

@api_view(["GET"])
def status(request: HttpRequest):
    global sistema_averiado
    sistema_averiado = random.choice(list(SISTEMAS_AVERIADOS.items()))[0]
    return Response({"damaged_system": sistema_averiado}, status = http_status.HTTP_200_OK)

def repair_bay(request: HttpRequest):
    code = SISTEMAS_AVERIADOS[sistema_averiado]
    return render(request, "repair-bay.html", {"code": code})

@api_view(["POST"])
def teapot(request: HttpRequest):
    return Response(
        {"detail": "I'm a teapot"},
        status = http_status.HTTP_418_IM_A_TEAPOT
    )
