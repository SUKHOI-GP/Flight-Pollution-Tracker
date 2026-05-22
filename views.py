from django.shortcuts import render, redirect
from .models import Flight
from .forms import FlightForm
import httpx

fastAPI_URL = "http://localhost:8001"

def index(request):
    flights = Flight.objects.all()
    return render(request, 'index.html', {'flights': flights})
def add_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            flight = form.save(commit=False)

            start = f"{flight.start_lng},{flight.start_lat}"
            end = f"{flight.end_lng},{flight.end_lat}"
            response = httpx.get(f"{fastAPI_URL}/route", params={"start": start, "end": end})
            data = response.json()
            flight.distance_km = data.get("distance_km")
            flight.duration_min = data.get("duration_min")

            flight.save()
            return redirect('index')
    else:
        form = FlightForm()
    return render(request, 'add_flight.html', {'form': form})

def flight_detail(request, pk):
    flight = Flight.objects.get(pk=pk)
    return render(request, 'flight_detail.html', {'flight': flight})



