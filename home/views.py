from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.contrib.auth import logout, login, authenticate

from .models import Profile
from .forms import LoginForm, UserForm, UpdateProfileForm

# Create your views here.

class Inicio(generic.View):
    template_name = "home/inicio.html"
    context = {}
    form = LoginForm()

    def get(self, request):
        self.context = {
            "form": self.form
        }
        return render(request, self.template_name, self.context)
    
    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/')
    
class Ubicacion(generic.View):
    template_name = "home/ubicacion.html"
    context = {}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
    
class Nosotros(generic.View):
    template_name = "home/nosotros.html"
    context = {}

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.context)
    
#-------------------------------------------------------
        
class Logout(generic.View):
    def get(self, request):
        logout(request)
        return redirect('/')
    
#-------------------------------------------- IDK

class SignUp(generic.CreateView):
    template_name = "home/signup.html"
    form_class = UserForm
    success_url = reverse_lazy("home:inicio")

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get("username")
        password1 = form.cleaned_data.get("password1")
        user = authenticate(self.request, username=username, password=password1)
        if user is not None:
            login(self.request, user)
        id = form.cleaned_data.get("id")
        print(id)
        return redirect("home:inicio")

class DetailProfile(generic.View):
    template_name = "home/detail_profile.html"
    context = {}

    def get(self, request, pk):
        self.context = {
            "profile": Profile.objects.get(id=pk)
        }
        return render(request, self.template_name, self.context)

class UpdateProfile(generic.UpdateView):
    template_name = "home/update_profile.html"
    model = Profile
    form_class = UpdateProfileForm
    success_url = reverse_lazy("home:detail_profile")

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("home:detail_profile", kwargs={"pk":pk})
