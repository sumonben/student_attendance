from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View, TemplateView, DetailView
from student.models import Student
from .models import Attendance,DailyAttendance
from django.http import JsonResponse
from datetime import date 
from django.contrib.auth.decorators import login_required
# Create your views here.
class StudentAttendanceView(View):
    template_name = 'attendance/student_attendance.html'
    
    def get(self, request, *args, **kwargs):
        context={}
        if request.user.is_authenticated:
            return render(request, self.template_name,context)
        else:
            return render(request, 'registration/login.html') 

    def post(self, request, *args, **kwargs):
        context={}
    
        if request.user.is_authenticated :
            return render(request, self.template_name,context)
        else:
            return render(request, 'registration/login.html')

class GetStudentView(View):
    template_name = 'attendance/student_attendance.html'
    
    
    def get(self, request, *args, **kwargs):
        context={}
        return render(request, self.template_name,context)
    
    def post(self, request, *args, **kwargs):
        context={}
        if request.POST.get('id')=='id_roll' :
            print("value",request.POST.get('value'))
            students=Student.objects.filter(class_roll=request.POST.get('value'))
            student=Student.objects.filter(class_roll=request.POST.get('value')).first()
            group=student.group.title_en
            session=student.session.title_en
            
                
                
            attendance=Attendance.objects.filter(class_roll=request.POST.get('value'), date=date.today()).first()
            done=0
            if attendance:
                done=1
            attendance1={}
            if student and attendance is None:
                    Attendance.objects.create(name=student.name,class_roll=student.class_roll,student=student,group=student.group,section=student.section,session=student.session,department=student.department)
                    daily_date=DailyAttendance.objects.filter(date=date.today(),session=student.session).first()
                    #print(daily_date)
                    if daily_date:
                        if student.group.title_en== "Science":
                            #print("Sciemve")
                            daily_date.science += 1
                        if student.group.title_en== "Humanities":
                            daily_date.humanities+=1
                        if student.group.title_en== "Business Studies":
                            daily_date.business_studies+=1
                        daily_date.all += 1
                        daily_date.save()
                    else:
                        science=0
                        humanities=0
                        business_studies=0
                        if student.group.title_en== "Science":
                            print("Sciemve")
                            science = 1
                        if student.group.title_en== "Humanities":
                            humanities=1
                        if student.group.title_en== "Business Studies":
                            business_studies=1
                        DailyAttendance.objects.create(date=date.today(),science=science,humanities=humanities,business_studies=business_studies,all=1,session=student.session)
                        
        student=list(students.values())
        attendance1=DailyAttendance.objects.filter(date=date.today())
        attendance1=list(attendance1.values())
           
        return JsonResponse({'status': 'success','meaasge':'Account created Successfully','student':student,'group':group,'session':session,'attendance1':attendance1,'done':done},safe=False)

def user_login(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('attendance') # Redirect to a success page
            else:
                # Handle invalid credentials
                return render(request, 'registration/login.html', {'message': 'Invalid credentials'})
        else:
            return render(request, 'registration/login.html') 