from django.http import HttpResponse
import datetime

def Saludo(request):

    return HttpResponse("Hola  mundo ")
#Primera vesta  que devuelve una respuesta y hace aparecer el texto

def IngresarDatos(request):
    return HttpResponse("Ingresa tus datos...")


def fecha_Y_Hora(request):
    """Fucion para Saber la hora actual por  Medio de Django """
    
    fecha_Actual=datetime.datetime.now() 
    return HttpResponse (fecha_Actual)  


def calcular_Edad(request,edad,anio):
    """ Fucion para calcular edad 
    en la web por medio del Framework Django """
    
    periodo = anio - 2019
    edad_futura = edad + periodo

    ducumento = f""" <html><body> <h2> Tu edad es de {edad} En el año {anio} tendras {edad_futura} años """
    return HttpResponse (ducumento)




    
    
