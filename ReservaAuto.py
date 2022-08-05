from select import select
from threading import local
from selenium import webdriver
from selenium.webdriver.support.select import Select
from datetime import date, timedelta
from datetime import datetime
import time 

Hoy = date.today()
Tiempo = datetime.now()
Manana = Hoy + timedelta(days=1)
FechaManana = Manana.strftime("%d/%m/%Y")
FechaHoy = Hoy.strftime("%d/%m/%Y")


print ("La fecha es: ", FechaHoy)
print ("Fecha mañana", FechaManana)

Hora = Tiempo.strftime("%H:%M")

if ("06:59">=Hora>="06:00"):
    print ("La hora es: ", Hora)
    Hora = "07:00"
    print ("Pero si lo redondeamos", Hora)
elif ("07:59">=Hora>="07:00"):
    print ("La hora es: ", Hora)
    Hora = "08:00"
    print ("Pero si lo redondeamos", Hora)
elif ("08:59">=Hora>="08:00"):
    print ("La hora es: ", Hora)
    Hora = "09:00"
    print ("Pero si lo redondeamos", Hora)
elif ("09:59">=Hora>="09:00"):
    print ("La hora es: ", Hora)
    Hora = "10:00"
    print ("Pero si lo redondeamos", Hora)
elif ("10:59">=Hora>="10:00"):
    print ("La hora es: ", Hora)
    Hora = "11:00"
    print ("Pero si lo redondeamos", Hora)
elif ("11:59">=Hora>="11:00"):
    print ("La hora es: ", Hora)
    Hora = "12:00"
    print ("Pero si lo redondeamos", Hora)
elif ("12:59">=Hora>="12:00"):
    print ("La hora es: ", Hora)
    Hora = "13:00"
    print ("Pero si lo redondeamos", Hora)
elif ("13:59">=Hora>="13:00"):
    print ("La hora es: ", Hora)
    Hora = "14:00"
    print ("Pero si lo redondeamos", Hora)
elif ("14:59">=Hora>="14:00"):
    print ("La hora es: ", Hora)
    Hora = "15:00"
    print ("Pero si lo redondeamos", Hora)
elif ("15:59">=Hora>="15:00"):
    print ("La hora es: ", Hora)
    Hora = "16:00"
    print ("Pero si lo redondeamos", Hora)
elif ("16:59">=Hora>="16:00" ):
    print ("La hora es: ", Hora)
    Hora = "17:00"
    print ("Pero si lo redondeamos", Hora)
elif ("17:59">=Hora>="17:00" ):
    print ("La hora es: ", Hora)
    Hora = "18:00"
    print ("Pero si lo redondeamos", Hora)
elif ("18:59">=Hora>="18:00" ):
    print ("La hora es: ", Hora)
    Hora = "19:00"
    print ("Pero si lo redondeamos", Hora)
elif ("19:59">=Hora>="19:00" ):
    print ("La hora es: ", Hora)
    Hora = "20:00"
    print ("Pero si lo redondeamos", Hora)
elif ("20:59">=Hora>="20:00" ):
    print ("La hora es: ", Hora)
    Hora = "21:00"
    print ("Pero si lo redondeamos", Hora)
elif (Hora>="21:00" ):
    print ("La hora es: ", Hora)
    print ("No podemos reservar para el día de hoy, lo haremos para mañana")
    Hora = "07:00"
    FechaHoy = FechaManana


web = webdriver.Chrome()
web.get('https://gimnasiopacific.cl/agendar-entrenamiento/paso1')

last = web.find_element("xpath",'//*[@id="local"]')
LocalOrigen = Select(last)
LocalOrigen.select_by_value("33")
last = web.find_element("xpath",'//*[@id="rut"]')
last.send_keys("")#Aqui va el rut
last = web.find_element("xpath",'//*[@id="localDestiny"]')
LocalDestino = Select(last)
LocalDestino.select_by_value("56")
time.sleep(2) 

Siguiente = web.find_element("xpath",'//*[@id="section_to_show"]/form/div[4]/button')
Siguiente.click()
time.sleep(2)
last = web.find_element("xpath",'//*[@id="scheduling_date"]')
last.send_keys(FechaHoy+"\n")


last = web.find_element("xpath",'//*[@id="scheduling_hour"]')
HoraElegida = Select(last)
HoraElegida.select_by_value(Hora)

Siguiente = web.find_element("xpath",'//*[@id="site-content"]/section/form/div[3]/button')
Siguiente.click()

print("Agendamiento Realizado :)")
input("Presiona un boton para continuar")