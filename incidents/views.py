from django.shortcuts import render, redirect, get_object_or_404
from .models import Incident


# P1 — Dashboard (List all incidents)
def index(request):
    incidents = Incident.objects.all().order_by('-created_at')
    return render(
        request,
        'incidents/index.html',
        {'incidents': incidents}
    )


# P2 — Create Incident
def create_incident(request):
    if request.method == 'POST':
        Incident.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            severity=request.POST.get('severity'),
            location=request.POST.get('location'),
            reported_by=request.POST.get('reported_by')
        )
        return redirect('/')

    return render(
        request,
        'incidents/create.html'
    )


# P3 — Update Incident
def update_incident(request, incident_id):
    incident = get_object_or_404(Incident, id=incident_id)

    if request.method == 'POST':
        incident.title = request.POST.get('title')
        incident.description = request.POST.get('description')
        incident.severity = request.POST.get('severity')
        incident.location = request.POST.get('location')
        incident.reported_by = request.POST.get('reported_by')
        incident.save()

        return redirect('/')

    return render(
        request,
        'incidents/update.html',
        {'incident': incident}
    )


# P4 — Delete Incident
def delete_incident(request, incident_id):
    incident = get_object_or_404(Incident, id=incident_id)

    if request.method == 'POST':
        incident.delete()
        return redirect('/')

    return render(
        request,
        'incidents/delete.html',
        {'incident': incident}
    )