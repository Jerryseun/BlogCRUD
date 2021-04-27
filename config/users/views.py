from django.shortcuts import render
from .forms import RegistrationForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = RegistrationForm()

    context = {'form': form}
    return render(request, 'users/register.html ', context)



"""from django.views.generic import RegisterView
from .models import Post

# Create your views here.
class UserRegisterView(RegisterView):
    model = Post
    template_name = 'user_register.html'"""
