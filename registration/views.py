from django.shortcuts import redirect, render
from django.contrib.auth.models import auth
from .forms import EmployeeForm,PatientForm,UpdatePatientForm
from .models import Patient,Employee
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return render(request,'index.html')

def showpatient(request):  
    patient=Patient.objects.all()
    
    return render(request,"dashboard.html",{'patient':patient})

def showemployee(request):  
    employee=Employee.objects.all()
    return render(request,"employeelist.html",{'employee':employee})

def dashboard1(request):
    return render(request,'dashboard.html')
# def appointment(request):
#     return render(request,'patient.html')

def registration(request):
    context = {}
    context['form'] = EmployeeForm()

    if request.method == 'POST':
        form = EmployeeForm(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('signup')
        else:
            context['form'] = form
    return render(request,'employee.html',context)

def patientregistration(request):
    context = {}
    context['form'] = PatientForm()

    if request.method == 'POST':
        form = PatientForm(request.POST,request.FILES)
        if(form.is_valid()):
            form.save()
            return redirect('patientregistration')
        else:
            context['form'] = form
    return render(request,'patient.html',context)

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				print(user.is_staff)
				if user.is_staff == True:
					return redirect("dashboard1")
				else:
					return redirect("index")

			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})
# @login_required
# def showpatient(request):  
#     patient=Patient.objects.all()
#     return render(request,"admin.html",{'patient':patient})
    

def updatepatient(request, id):  
    patient = Patient.objects.get(id=id) 
    form  = UpdatePatientForm(instance=patient)
    if request.method == 'POST':
            form  = UpdatePatientForm(request.POST,instance=patient)
            if form.is_valid():
                form.save()
                return redirect("/showpatient") 
    return render(request, 'editpatient.html', {'patient_form':form })  

def admindashboard(request):
    return render(request, 'admin.html')