import imp
from django.contrib.auth.models import User,Group
from django import forms

class UserForm(forms.ModelForm):
    password  = forms.CharField(widget=forms.PasswordInput)
    role = forms.ModelChoiceField(queryset=Group.objects.all())

    class Meta:
        model = User
        fields = ['first_name' , 'last_name','email' , 'username' , 'password']
        lables = {
            'password' : 'password'
        }
        #excludes = []
    
    def __init__(self,*args,**kwargs):
        if kwargs.get('instance'):
            initial = kwargs.setdefault('initial' , {})

            if kwargs['instance'].groups.all():
                initial['role'] = kwargs['instance'].groups.all()[0]
            else:
                initial['role'] = None
        
        forms.ModelForm.__init__(self,*args,**kwargs)

    def clean_email(self):
        if self.cleaned_data["email"].endswith("@a.com"):
            return self.cleaned_data['email']
        else:
            raise forms.ValidationError("Email is not correct")

    def save(self):
        password = self.cleaned_data.pop("password")
        role = self.cleaned_data.pop("role")

        u = super().save()
        u.set_password(password)
        u.groups.set([role])
        u.save()

