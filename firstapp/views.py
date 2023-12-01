from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.core.exceptions import ValidationError
from .forms import ContactForm
from django.views.generic.edit import CreateView
from .forms import RegistrationForm



# Create your views here.
def index(request):
    age =10
    arr =['hey','you']
    return render(request,'firstapp/index.html',{"age":age,"arr":arr})

# class Index(TemplateView):
#     template_name = 'firstapp/index.html'
#     def get_context_data(self, **kwargs):
#         age =10
#         arr =['hey','you']
#         context_old = super().get_context_data(**kwargs)
#         context = {"age":age,"arr":arr, " context_old":context_old}
#         return context



#     if request.method == "POST":
#         name = request.POST.get('name')
#         email = request.POST.get('email')
#         # phone = request.POST.get('phone')
#         if len(phone)<10 or len(phone)>10:
#             return ValidationError("Problem with phone number.")
#         phone = request.POST['phone']
#         query = request.POST.get('query')
#     return render(request,'firstapp/contact.html')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            if len(form.cleaned_data.get('query'))>10:
                form.add_error('query','Query length is not right')
                return render(request,'firstapp/contact.html',{'form':form})
            form.save()
            return HttpResponse("Thank you")
        else:
            if len(form.cleaned_data.get('query'))>10:
                form.add_error('query','Query length is not right')
                form.errors['__all__'] = "query length is not right."
            return render(request,'firstapp/contact.html',{'form':form})
    return render(request,'firstapp/contact.html',{'form':ContactForm})

class RegisterView(CreateView):
    template_name = "firstapp/register.html"
    form_class = RegistrationForm
    success_url = reverse_lazy('index')

def testsessions(request):
    if request.session.get('test',False):
        print(request.session['test'])

    request.session.set_expiry(1)
    request.session['test'] = 'hello'
    return render(request,'firstapp/sessiontesting.html')