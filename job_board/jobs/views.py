from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Job

@login_required
def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

@login_required
def job_detail(request, job_id):
    job = Job.objects.get(pk=job_id)
    # Aquí puedes agregar la lógica para manejar el envío de solicitudes de empleo
    return render(request, 'jobs/job_detail.html', {'job': job})
