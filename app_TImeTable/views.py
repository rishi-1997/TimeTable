from django.shortcuts import render,redirect
from .models import TimeTable
from app_TImeTable import forms
from app_TImeTable.forms import TimeTableForm
# Create your views here.

def index_view(request):
    timetable = TimeTable.objects.all()
    return render(request,'Time_Table_app/index.html',{'timetable':timetable})

def create_view(request):
    form = forms.TimeTableForm()
    if request.method=='POST':
        form = forms.TimeTableForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'Time_Table_app/create.html',{'form':form})

def delete_view(request,id):
    timetable = TimeTable.objects.get(id=id)
    timetable.delete()
    return redirect('/')

def update_views(request,id):
    timetable = TimeTable.objects.get(id=id)
    if request.method == 'POST':
        form = TimeTableForm(request.POST,instance=timetable)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request,'Time_Table_app/update.html',{'timetable':timetable})