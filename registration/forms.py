from django import forms
from .models import Employee,Patient
from django.forms  import ValidationError
class EmployeeForm(forms.ModelForm):
    GENDER  = (
        ('Male','Male'),
        ('Female','Female')
    )
    username = forms.CharField()
    email = forms.EmailField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    gender = forms.CharField(widget=forms.Select(choices=GENDER))
    phone=forms.IntegerField()
    image = forms.ImageField()
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())


    class Meta:
        # model = employee
        # fields = ("FullName","mobile_no","emp_code","position")
        # widgets={
        #     'FullName':forms.TextInput(attrs={'class':'form-control','id':'fullName','placeholder':'Full Name'}),
        #     'mobile_no':forms.TextInput(attrs={'class':'form-control','id':'mobNo','placeholder':'Mobile Number'}),
        #     'emp_code':forms.TextInput(attrs={'class':'form-control','id':'emp_code','placeholder':'Emp. Code'}),
        #     'position':forms.Select(attrs={'class':'form-control','id':'exampleFormControlSelect1'}),
        # }
        model = Employee
        fields = ('first_name','last_name','username','email','gender','phone','image','password','confirm_password')
    def clean(self):
        errors=[]
        first_name = self.cleaned_data['first_name']
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if(password != confirm_password):
            errors.append("Password doesn't match")
        
        if(len(first_name)< 2):
            errors.append("Fistname is too short")
        if(len(username)< 2):
            errors.append("Username is too short")

        if(len(errors) > 0):
            raise ValidationError(errors)

    
    def save(self):
        employee  = Employee(first_name = self.cleaned_data['first_name'],last_name = self.cleaned_data['last_name'],username = self.cleaned_data['username'],email= self.cleaned_data['email'],gender= self.cleaned_data['gender'],phone=self.cleaned_data['phone'],image=self.cleaned_data['image'])
        employee.set_password(self.cleaned_data['password'])
        employee.save()
        return employee

class PatientForm(forms.ModelForm):
    class Meta:
        model=Patient
        fields=['first_name','last_name','gender','phone','appointment_date']

class UpdatePatientForm(forms.ModelForm):
    GENDER = (
        ('Male', 'Male'),
        ('Female', 'Female')
    )
    first_name = forms.CharField()
    last_name = forms.CharField()
    gender = forms.CharField(widget=forms.Select(choices=GENDER), required=True)
    phone = forms.IntegerField(required=True)
    appointment_date=forms.DateField()

    class Meta:
        model = Patient
        fields = ['first_name','last_name','gender','phone','appointment_date']