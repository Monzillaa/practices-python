from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta

# La fecha puede venir de now, o puedes parsearla como veremos más abajo
ahora = datetime.now()
print("Ahora: " + str(ahora))
hace_una_semana = ahora - timedelta(days=7)
print("Hace una semana: " + str(hace_una_semana))
# Recuerda que puedes formatearla.
hace_una_semana_formateada = hace_una_semana.strftime("%Y-%m-%d")
print("Hace una semana, solo fecha: " + hace_una_semana_formateada)

# Ahora sumar algunas horas. Vamos a parsear la fecha:
fechaCadena = "2020-04-22 00:00:00"
ahora = datetime.strptime(fechaCadena, '%Y-%m-%d %H:%M:%S')
print("Ahora: " + str(ahora))
dentro_de_1_hora = ahora + timedelta(hours=1)
print("Dentro de una hora: " + str(dentro_de_1_hora))

"""
Comienza el uso de relativedelta. Recuerda instalar con:
pip install python-dateutil
"""

dentro_de_un_mes = ahora + relativedelta(months=1)
print("Dentro de un mes: " + str(dentro_de_un_mes))


dentro_de_anio_y_semana = ahora + relativedelta(years=1, weeks=1)
print("Dentro de un año y una semana: " + str(dentro_de_anio_y_semana))

# Sumar pero con negativos, obteniendo una resta

hace_dos_anios = ahora + relativedelta(years=-2)
print("Hace dos años: " + str(hace_dos_anios))