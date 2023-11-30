from django.shortcuts import render

from django.views import generic
from django.urls import reverse_lazy

# from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Recamara, Bano, Cocina, Comedor, Sala, Oficina
from .forms import RecamaraForm, UpdateRecamaraForm, BanoForm, UpdateBanoForm, CocinaForm, UpdateCocinaForm, ComedorForm, UpdateComedorForm, SalaForm, UpdateSalaForm, OficinaForm, UpdateOficinaForm

# Create your views here.

#------------------------------------------ CRUD RECAMARA -------------------------------------------#
#List
class ListRecamara(generic.View):
    template_name = "core/recamara/list_recamara.html"
    context = {}
    login_url = reverse_lazy("home:inicio")

    def get(self, request, *args, **kwargs):
        recamaras = Recamara.objects.filter(status=True)
        self.context = {
            "recamaras": recamaras
        }
        return render(request, self.template_name, self.context)

#Detail
class DetailRecamara(generic.View):
    template_name = "core/recamara/detail_recamara.html"
    context = {}
    login_url = reverse_lazy("home:inicio")

    def get(self, request, pk, *args, **kwargs):
        recamara = Recamara.objects.get(pk=pk)
        self.context = {
            "recamara": recamara
        }
        return render(request, self.template_name, self.context)

#Create
class CreateRecamara(generic.CreateView):
    template_name = "core/recamara/create_recamara.html"
    model = Recamara
    form_class = RecamaraForm
    success_url = reverse_lazy("core:list_recamara")
    login_url = reverse_lazy("home:inicio")

#Update
class UpdateRecamara(generic.UpdateView):
    template_name = "core/recamara/update_recamara.html"
    model = Recamara
    form_class = UpdateRecamaraForm
    success_url = reverse_lazy("core:list_recamara")
    login_url = reverse_lazy("home:inicio")

#Delete
class DeleteRecamara(generic.DeleteView):
    template_name = "core/recamara/delete_recamara.html"
    model = Recamara
    success_url = reverse_lazy("core:list_recamara")
    login_url = reverse_lazy("home:inicio")

#------------------------------------------ CRUD BATHROOM -------------------------------------------#
#List
class ListBano(generic.View):
    template_name = "core/bano/list_bano.html"
    login_url = reverse_lazy("home:inicio")

    def get(self, request, *args, **kwargs):
        banos = Bano.objects.filter(status=True)
        return render(request, self.template_name, {'banos': banos})

#Detail
class DetailBano(generic.View):
    template_name = "core/bano/detail_bano.html"
    context = {}
    login_url = reverse_lazy("home:inicio")

    def get(self, request, pk, *args, **kwargs):
        bano = Bano.objects.get(pk=pk)
        self.context = {
            "bano": bano
        }
        return render(request, self.template_name, self.context)

#Create
class CreateBano(generic.CreateView):
    template_name = "core/bano/create_bano.html"
    model = Bano
    form_class = BanoForm
    success_url = reverse_lazy("core:list_bano")
    login_url = reverse_lazy("home:inicio")

#Update
class UpdateBano(generic.UpdateView):
    template_name = "core/bano/update_bano.html"
    model = Bano
    form_class = UpdateBanoForm
    success_url = reverse_lazy("core:list_bano")
    login_url = reverse_lazy("home:inicio")

#Delete
class DeleteBano(generic.DeleteView):
    template_name = "core/bano/delete_bano.html"
    model = Bano
    success_url = reverse_lazy("core:list_bano")
    login_url = reverse_lazy("home:inicio")

#------------------------------------------ CRUD COCINA -------------------------------------------#
#List
class ListCocina(generic.View):
    template_name = "core/cocina/list_cocina.html"
    context = {}
    login_url = reverse_lazy("home:inicio")

    def get(self, request, *args, **kwargs):
        cocinas = Cocina.objects.filter(status=True)
        self.context = {
            "cocinas": cocinas
        }
        return render(request, self.template_name, self.context)

#Detail
class DetailCocina(generic.View):
    template_name = "core/cocina/detail_cocina.html"
    context = {}
    login_url = reverse_lazy("home:inicio")

    def get(self, request, pk, *args, **kwargs):
        cocina = Cocina.objects.get(pk=pk)
        self.context = {
            "cocina": cocina
        }
        return render(request, self.template_name, self.context)

#Create
class CreateCocina(generic.CreateView):
    template_name = "core/cocina/create_cocina.html"
    model = Cocina
    form_class = CocinaForm
    success_url = reverse_lazy("core:list_cocina")
    login_url = reverse_lazy("home:inicio")

#Update
class UpdateCocina(generic.UpdateView):
    template_name = "core/cocina/update_cocina.html"
    model = Cocina
    form_class = UpdateCocinaForm
    success_url = reverse_lazy("core:list_cocina")
    login_url = reverse_lazy("home:inicio")

#Delete
class DeleteCocina(generic.DeleteView):
    template_name = "core/cocina/delete_cocina.html"
    model = Cocina
    success_url = reverse_lazy("core:list_cocina")
    login_url = reverse_lazy("home:inicio")

#------------------------------------------ CRUD COMEDOR -------------------------------------------#
#List
class ListComedor(generic.View):
    template_name = "core/comedor/list_comedor.html"
    context = {}
    login_url = reverse_lazy("home:inicio")

    def get(self, request, *args, **kwargs):
        comedores = Comedor.objects.filter(status=True)
        self.context = {
            "comedores": comedores
        }
        return render(request, self.template_name, self.context)

#Detail
class DetailComedor(generic.View):
    template_name = "core/comedor/detail_comedor.html"
    context = {}
    login_url = reverse_lazy("home:inicio")

    def get(self, request, pk, *args, **kwargs):
        comedor = Comedor.objects.get(pk=pk)
        self.context = {
            "comedor": comedor
        }
        return render(request, self.template_name, self.context)

#Create
class CreateComedor(generic.CreateView):
    template_name = "core/comedor/create_comedor.html"
    model = Comedor
    form_class = ComedorForm
    success_url = reverse_lazy("core:list_comedor")
    login_url = reverse_lazy("home:inicio")

#Update
class UpdateComedor(generic.UpdateView):
    template_name = "core/comedor/update_comedor.html"
    model = Comedor
    form_class = UpdateComedorForm
    success_url = reverse_lazy("core:list_comedor")
    login_url = reverse_lazy("home:inicio")

#Delete
class DeleteComedor(generic.DeleteView):
    template_name = "core/comedor/delete_comedor.html"
    model = Comedor
    success_url = reverse_lazy("core:list_comedor")
    login_url = reverse_lazy("home:inicio")

#------------------------------------------ CRUD SALA -------------------------------------------#
#List
class ListSala(generic.View):
    template_name = "core/sala/list_sala.html"
    context = {}
    login_url = reverse_lazy("home:inicio")

    def get(self, request, *args, **kwargs):
        salas = Sala.objects.filter(status=True)
        self.context = {
            "salas": salas
        }
        return render(request, self.template_name, self.context)

#Detail
class DetailSala(generic.View):
    template_name = "core/sala/detail_sala.html"
    context = {}
    login_url = reverse_lazy("home:inicio")

    def get(self, request, pk, *args, **kwargs):
        sala = Sala.objects.get(pk=pk)
        self.context = {
            "sala": sala
        }
        return render(request, self.template_name, self.context)

#Create
class CreateSala(generic.CreateView):
    template_name = "core/sala/create_sala.html"
    model = Sala
    form_class = SalaForm
    success_url = reverse_lazy("core:list_sala")
    login_url = reverse_lazy("home:inicio")

#Update
class UpdateSala(generic.UpdateView):
    template_name = "core/sala/update_sala.html"
    model = Sala
    form_class = UpdateSalaForm
    success_url = reverse_lazy("core:list_sala")
    login_url = reverse_lazy("home:inicio")

#Delete
class DeleteSala(generic.DeleteView):
    template_name = "core/sala/delete_sala.html"
    model = Sala
    success_url = reverse_lazy("core:list_sala")
    login_url = reverse_lazy("home:inicio")

#------------------------------------------ CRUD OFICINA -------------------------------------------#
#List
class ListOficina(generic.View):
    template_name = "core/oficina/list_oficina.html"
    context = {}
    login_url = reverse_lazy("home:inicio")

    def get(self, request, *args, **kwargs):
        oficinas = Oficina.objects.filter(status=True)
        self.context = {
            "oficinas": oficinas
        }
        return render(request, self.template_name, self.context)

#Detail
class DetailOficina(generic.View):
    template_name = "core/oficina/detail_oficina.html"
    context = {}
    login_url = reverse_lazy("home:inicio")

    def get(self, request, pk, *args, **kwargs):
        oficina = Oficina.objects.get(pk=pk)
        self.context = {
            "oficina": oficina
        }
        return render(request, self.template_name, self.context)

#Create
class CreateOficina(generic.CreateView):
    template_name = "core/oficina/create_oficina.html"
    model = Oficina
    form_class = OficinaForm
    success_url = reverse_lazy("core:list_oficina")
    login_url = reverse_lazy("home:inicio")

#Update
class UpdateOficina(generic.UpdateView):
    template_name = "core/oficina/update_oficina.html"
    model = Oficina
    form_class = UpdateOficinaForm
    success_url = reverse_lazy("core:list_oficina")
    login_url = reverse_lazy("home:inicio")

#Delete
class DeleteOficina(generic.DeleteView):
    template_name = "core/oficina/delete_oficina.html"
    model = Oficina
    success_url = reverse_lazy("core:list_oficina")
    login_url = reverse_lazy("home:inicio")
