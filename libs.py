
from datetime import datetime


def calcular_edad(fecha):
    return (fecha.date() - datetime.now()).year


def preguntar_nombre():
    return input("Ingrese su nombre: ")
