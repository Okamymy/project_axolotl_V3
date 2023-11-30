from django import forms

from .models import Recamara, Bano, Cocina, Comedor, Sala, Oficina

# -------------------------------------------- RECAMARA -------------------------------------------------- #

class RecamaraForm(forms.ModelForm):
    class Meta:
        model = Recamara
        fields = [
            "recamara_name",
            "imagen",
            "descripcion",
            "stock",
            "precio",
            "status",
            "codigo",
        ]

        widgets = {
            "recamara_name": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el nombre"}),
            "imagen": forms.FileInput(attrs={"type":"file", "class":"form-control"}),
            "descripcion": forms.Textarea(attrs={"type":"text", "class":"form-control", "rows":3, "placeholder":"Escribe una descripcion"}),
            "stock": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "precio": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "status": forms.CheckboxInput(attrs={"type":"checkbox"}),
            "codigo": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el código de busqueda"})
        }

class UpdateRecamaraForm(forms.ModelForm):
    class Meta:
        model = Recamara
        fields = [
            "recamara_name",
            "imagen",
            "descripcion",
            "stock",
            "precio",
            "status",
            "codigo",
        ]

        widgets = {
            "recamara_name": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el nombre"}),
            "imagen": forms.FileInput(attrs={"type":"file", "class":"form-control"}),
            "descripcion": forms.Textarea(attrs={"type":"text", "class":"form-control", "rows":3, "placeholder":"Escribe una descripcion"}),
            "stock": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "precio": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "status": forms.CheckboxInput(attrs={"type":"checkbox"}),
            "codigo": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el código de busqueda"})
        }

# -------------------------------------------- BAÑO -------------------------------------------------- #

class BanoForm(forms.ModelForm):
    class Meta:
        model = Bano
        fields = [
            "bano_name",
            "imagen",
            "descripcion",
            "stock",
            "precio",
            "status",
            "codigo",
        ]

        widgets = {
            "bano_name": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el nombre"}),
            "imagen": forms.FileInput(attrs={"type":"file", "class":"form-control"}),
            "descripcion": forms.Textarea(attrs={"type":"text", "class":"form-control", "rows":3, "placeholder":"Escribe una descripcion"}),
            "stock": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "precio": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "status": forms.CheckboxInput(attrs={"type":"checkbox"}),
            "codigo": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el código de busqueda"})
        }

class UpdateBanoForm(forms.ModelForm):
    class Meta:
        model = Bano
        fields = [
            "bano_name",
            "imagen",
            "descripcion",
            "stock",
            "precio",
            "status",
            "codigo",
        ]

        widgets = {
            "bano_name": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el nombre"}),
            "imagen": forms.FileInput(attrs={"type":"file", "class":"form-control"}),
            "descripcion": forms.Textarea(attrs={"type":"text", "class":"form-control", "rows":3, "placeholder":"Escribe una descripcion"}),
            "stock": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "precio": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "status": forms.CheckboxInput(attrs={"type":"checkbox"}),
            "codigo": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el código de busqueda"})
        }

# -------------------------------------------- COCINA -------------------------------------------------- #

class CocinaForm(forms.ModelForm):
    class Meta:
        model = Cocina
        fields = [
            "cocina_name",
            "imagen",
            "descripcion",
            "stock",
            "precio",
            "status",
            "codigo",
        ]

        widgets = {
            "cocina_name": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el nombre"}),
            "imagen": forms.FileInput(attrs={"type":"file", "class":"form-control"}),
            "descripcion": forms.Textarea(attrs={"type":"text", "class":"form-control", "rows":3, "placeholder":"Escribe una descripcion"}),
            "stock": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "precio": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "status": forms.CheckboxInput(attrs={"type":"checkbox"}),
            "codigo": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el código de busqueda"})
        }

class UpdateCocinaForm(forms.ModelForm):
    class Meta:
        model = Cocina
        fields = [
            "cocina_name",
            "imagen",
            "descripcion",
            "stock",
            "precio",
            "status",
            "codigo",
        ]

        widgets = {
            "cocina_name": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el nombre"}),
            "imagen": forms.FileInput(attrs={"type":"file", "class":"form-control"}),
            "descripcion": forms.Textarea(attrs={"type":"text", "class":"form-control", "rows":3, "placeholder":"Escribe una descripcion"}),
            "stock": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "precio": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "status": forms.CheckboxInput(attrs={"type":"checkbox"}),
            "codigo": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el código de busqueda"})
        }

# -------------------------------------------- COMEDOR -------------------------------------------------- #

class ComedorForm(forms.ModelForm):
    class Meta:
        model = Comedor
        fields = [
            "comedor_name",
            "imagen",
            "descripcion",
            "stock",
            "precio",
            "status",
            "codigo",
        ]

        widgets = {
            "comedor_name": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el nombre"}),
            "imagen": forms.FileInput(attrs={"type":"file", "class":"form-control"}),
            "descripcion": forms.Textarea(attrs={"type":"text", "class":"form-control", "rows":3, "placeholder":"Escribe una descripcion"}),
            "stock": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "precio": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "status": forms.CheckboxInput(attrs={"type":"checkbox"}),
            "codigo": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el código de busqueda"})
        }

class UpdateComedorForm(forms.ModelForm):
    class Meta:
        model = Comedor
        fields = [
            "comedor_name",
            "imagen",
            "descripcion",
            "stock",
            "precio",
            "status",
            "codigo",
        ]

        widgets = {
            "comedor_name": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el nombre"}),
            "imagen": forms.FileInput(attrs={"type":"file", "class":"form-control"}),
            "descripcion": forms.Textarea(attrs={"type":"text", "class":"form-control", "rows":3, "placeholder":"Escribe una descripcion"}),
            "stock": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "precio": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "status": forms.CheckboxInput(attrs={"type":"checkbox"}),
            "codigo": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el código de busqueda"})
        }

# -------------------------------------------- SALA -------------------------------------------------- #

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = [
            "sala_name",
            "imagen",
            "descripcion",
            "stock",
            "precio",
            "status",
            "codigo",
        ]

        widgets = {
            "sala_name": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el nombre"}),
            "imagen": forms.FileInput(attrs={"type":"file", "class":"form-control"}),
            "descripcion": forms.Textarea(attrs={"type":"text", "class":"form-control", "rows":3, "placeholder":"Escribe una descripcion"}),
            "stock": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "precio": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "status": forms.CheckboxInput(attrs={"type":"checkbox"}),
            "codigo": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el código de busqueda"})
        }

class UpdateSalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = [
            "sala_name",
            "imagen",
            "descripcion",
            "stock",
            "precio",
            "status",
            "codigo",
        ]

        widgets = {
            "sala_name": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el nombre"}),
            "imagen": forms.FileInput(attrs={"type":"file", "class":"form-control"}),
            "descripcion": forms.Textarea(attrs={"type":"text", "class":"form-control", "rows":3, "placeholder":"Escribe una descripcion"}),
            "stock": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "precio": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "status": forms.CheckboxInput(attrs={"type":"checkbox"}),
            "codigo": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el código de busqueda"})
        }

# -------------------------------------------- OFICINA -------------------------------------------------- #

class OficinaForm(forms.ModelForm):
    class Meta:
        model = Oficina
        fields = [
            "oficina_name",
            "imagen",
            "descripcion",
            "stock",
            "precio",
            "status",
            "codigo",
        ]

        widgets = {
            "oficina_name": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el nombre"}),
            "imagen": forms.FileInput(attrs={"type":"file", "class":"form-control"}),
            "descripcion": forms.Textarea(attrs={"type":"text", "class":"form-control", "rows":3, "placeholder":"Escribe una descripcion"}),
            "stock": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "precio": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "status": forms.CheckboxInput(attrs={"type":"checkbox"}),
            "codigo": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el código de busqueda"})
        }

class UpdateOficinaForm(forms.ModelForm):
    class Meta:
        model = Oficina
        fields = [
            "oficina_name",
            "imagen",
            "descripcion",
            "stock",
            "precio",
            "status",
            "codigo",
        ]

        widgets = {
            "oficina_name": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el nombre"}),
            "imagen": forms.FileInput(attrs={"type":"file", "class":"form-control"}),
            "descripcion": forms.Textarea(attrs={"type":"text", "class":"form-control", "rows":3, "placeholder":"Escribe una descripcion"}),
            "stock": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "precio": forms.TextInput(attrs={"type":"number", "class":"form-control"}),
            "status": forms.CheckboxInput(attrs={"type":"checkbox"}),
            "codigo": forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Escribe el código de busqueda"})
        }
