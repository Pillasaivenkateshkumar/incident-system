from django.shortcuts import render, redirect
from .models import Incident


def dashboard(request):
    incidents = Incident.objects.all().order_by('-created_at')

    p1_count = Incident.objects.filter(priority='P1').count()
    p2_count = Incident.objects.filter(priority='P2').count()
    p3_count = Incident.objects.filter(priority='P3').count()
    p4_count = Incident.objects.filter(priority='P4').count()

    resolved_count = Incident.objects.filter(status='RESOLVED').count()

    return render(request, 'incidents/dashboard.html', {
        'incidents': incidents,
        'p1_count': p1_count,
        'p2_count': p2_count,
        'p3_count': p3_count,
        'p4_count': p4_count,
        'resolved_count': resolved_count,
    })


def create_incident(request):
    if request.method == 'POST':
        Incident.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            location=request.POST['location'],
            reported_by=request.POST['reported_by'],
            priority=request.POST['priority'],
            status=request.POST['status']
        )
        return redirect('dashboard')

    return render(request, 'incidents/create.html')