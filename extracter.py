# -*- coding: utf-8 -*-
"""extracter.ipynb
Original file is located at
    https://colab.research.google.com/drive/1eJ7it5WB6koDK9ww60lYwf03ibhjrmHy
"""

from opensky_api import OpenSkyApi
import datetime
from opensky_api import TokenManager

"""El método `get_flights_by_aircraft` permite recuperar los vuelos de una aeronave específica en un intervalo de tiempo determinado. Para ello, especifique la dirección única de la aeronave ICAO de 24 bits en formato hexadecimal, así como el inicio y el final del intervalo de tiempo en forma de marcas de tiempo. El intervalo de tiempo debe ser inferior a 30 días. El siguiente ejemplo muestra los pasos a seguir para obtener los vuelos de la aeronave D-AIZZ (3c675a) del 29 de enero de 2018:"""

from opensky_api import OpenSkyApi
api = OpenSkyApi()
data = api.get_flights_by_aircraft("3c675a", 1517184000, 1517270400)
for flight in data:
    print(flight)

"""También es posible obtener vectores de estado para un área determinada. Para ello, es necesario proporcionar un cuadro delimitador, definido por los límites inferior y superior de longitud y latitud. El siguiente ejemplo muestra cómo obtener datos para un cuadro delimitador que abarca Suiza:"""

api = OpenSkyApi()
# bbox = (min latitude, max latitude, min longitude, max longitude)
states = api.get_states(bbox=(45.8389, 47.8229, 5.9962, 10.5226))
for s in states.states:
    print("(%r, %r, %r, %r)" % (s.longitude, s.latitude, s.baro_altitude, s.velocity))

"""Puedes recuperar datos de vuelo de un intervalo de tiempo específico utilizando el método `get_flights_from_interval`. Para ello, proporciona el inicio y el final del período como marcas de tiempo. Es importante que el intervalo de tiempo proporcionado no sea superior a 2 horas. El siguiente ejemplo muestra cómo recuperar los datos de vuelo desde las 12:00 hasta la 13:00 del 29 de enero de 2018:"""

api = OpenSkyApi()
data = api.get_flights_from_interval(1517227200, 1517230800)
for flight in data:
    print(flight)