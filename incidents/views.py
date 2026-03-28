from django.shortcuts import render, redirect, get_object_or_404
from .models import Incident

# DASHBOARD
def index(request):
    incidents = Incident.objects.all().order_by('-created_at')

    # ✅ COUNTS (IMPORTANT)
    p1_count = Incident.objects.filter(priority='Critical').count()
    p2_count = Incident.objects.filter(priority='High').count()
    p3_count = Incident.objects.filter(priority='Medium').count()
    p4_count = Incident.objects.filter(priority='Low').count()
    resolved_count = Incident.objects.filter(status='Resolved').count()

    return render(request, 'incidents/index.html', {
        'incidents': incidents,
        'p1_count': p1_count,
        'p2_count': p2_count,
        'p3_count': p3_count,
        'p4_count': p4_count,
        'resolved_count': resolved_count,
    })


# CREATE
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


# UPDATE
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


# DELETE
def delete_incident(request, id):
    incident = get_object_or_404(Incident, id=id)

    if request.method == 'POST':
        incident.delete()
        return redirect('index')

    return render(request, 'incidents/delete.html', {'incident': incident})