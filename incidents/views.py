from django.shortcuts import render, redirect, get_object_or_404
from .models import Incident


def index(request):
    incidents = Incident.objects.all().order_by('-created_at')

    context = {
        'incidents': incidents,
        'p1': incidents.filter(priority='P1').count(),
        'p2': incidents.filter(priority='P2').count(),
        'p3': incidents.filter(priority='P3').count(),
        'p4': incidents.filter(priority='P4').count(),
        'resolved': incidents.filter(status='RESOLVED').count(),
    }

    return render(request, 'incidents/index.html', context)


def create_incident(request):
    if request.method == 'POST':
        Incident.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            priority=request.POST['priority'],
            status=request.POST['status']
        )
        return redirect('index')

    return render(request, 'incidents/create.html')


def update_incident(request, id):
    incident = get_object_or_404(Incident, id=id)

    if request.method == 'POST':
        incident.title = request.POST['title']
        incident.description = request.POST['description']
        incident.priority = request.POST['priority']
        incident.status = request.POST['status']
        incident.save()
        return redirect('index')

    return render(request, 'incidents/update.html', {'incident': incident})


def delete_incident(request, id):
    incident = get_object_or_404(Incident, id=id)

    if request.method == 'POST':
        incident.delete()
        return redirect('index')

    return render(request, 'incidents/delete.html', {'incident': incident})