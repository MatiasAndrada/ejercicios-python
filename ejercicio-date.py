#Es necesario importar las dependencias necesarias
from datetime import date
from datetime import datetime

#Día actual
today = date.today()

#Fecha actual
now = datetime.now()

#formato personalizado
print("Hora actual: ", now.strftime("%H:%M"))

print(today)
print(now)