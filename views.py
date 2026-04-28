from django.shortcuts import render

def index(request):
    # Aquí puedes pasar datos de tu base de datos
    context = {
        'titulo': 'Bienvenido a mi sitio',
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')


