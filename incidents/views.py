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
        title = request.POST.get('title')
        description = request.POST.get('description')
        priority = request.POST.get('priority')  # 🔥 IMPORTANT
        status = request.POST.get('status')

        print("DEBUG PRIORITY:", priority)  # 👈 TEMP DEBUG

        Incident.objects.create(
            title=title,
            description=description,
            priority=priority,
            status=status
        )

        return redirect('index')

    return render(request, 'incidents/create.html')


# UPDATE
def update_incident(request, id):
    incident = get_object_or_404(Incident, id=id)

    if request.method == 'POST':
        incident.title = request.POST.get('title')
        incident.description = request.POST.get('description')
        incident.priority = request.POST.get('priority')   # ✅ IMPORTANT
        incident.status = request.POST.get('status')       # ✅ IMPORTANT

        print("UPDATED PRIORITY:", incident.priority)  # debug

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