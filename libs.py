
from datetime import datetime


def calcular_edad(fecha):
    return (datetime.now() - fecha.date()).year


def preguntar_nombre():
    return input("Ingrese su nombres: ")
