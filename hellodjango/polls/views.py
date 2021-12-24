from django.shortcuts import render, redirect
from polls.models import Subject, Teacher

def show_subject(request):
    subject = Subject.objects.all().order_by('no')
    return render(request, 'subject.html', {'subjects': subject})

def show_teacher(request):
    try:
        sno = int(request.GET.get('sno'))
        teachers = []
        if sno:
            subject = Subject.objects.only('name').get(no=sno)
            teachers = Teacher.objects.filter(subject=subject).order_by('no')
        return render(request,'teachers.html', {
            'subject': subject,
            'teachers': teachers
        })
    except (ValueError, Subject.DoesNotExist):
        return redirect('/')