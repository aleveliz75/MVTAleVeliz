from django.shortcuts import render

from MVTAPP.models import Familiares

def get_familiares(request):
    f1 = Familiares(nombre='Graciela', apellido='Rodriguez', edad=55, cumpleanios='1971-04-22', parentezco='Madre')
    f2 = Familiares(nombre='Cristian', apellido='Veliz', edad=61, cumpleanios='1966-11-06', parentezco='Padre')
    f3 = Familiares(nombre='Cinthia', apellido='Veliz', edad=31, cumpleanios='1991-09-22', parentezco='Hermana')

    return render(request, 'MVTAPP/Familiares.html', {'familiares': [f1, f2, f3]})