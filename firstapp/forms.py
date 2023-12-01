from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django import forms
from .models import CustomUser,Contact

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class ContactForm(forms.ModelForm):
    # email = forms.EmailField(required=True)
    # name = forms.CharField(max_length=10,required=True)
    # # regex code
    # regex = None
    # phone = forms.IntegerField(required=True,validator=[regex])
    # query = forms.CharField(widget = forms.Textarea )
    class Meta:
        model = Contact
        fields = [
            'email',
            'phone',
            'query',
            'name'
        ]

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields =[
            "email",
            "password1",
            "password2"
        ]