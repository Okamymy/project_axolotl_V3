from django.db import models

# Create your models here.

class Recamara(models.Model):
    recamara_name = models.CharField('Nombre:', max_length=50, default="Nombre Mueble Recamara")
    imagen = models.ImageField('Imagen:', upload_to='M-Recamara/', blank=False, null=False, default="/static/images/logos/Logo.png")
    descripcion = models.CharField('Descripcion:', max_length=256, default="Descripcion Mueble Recamara")
    stock = models.IntegerField('Stock:', default=0)
    precio = models.FloatField('Precio:', default=0.00)
    timestamp = models.DateField(auto_now_add=True)
    update_recamara = models.DateField(auto_now=True, auto_now_add=False)
    status = models.BooleanField('Estado:', default=True)
    codigo = models.SlugField('Código:', max_length=16)

    def __str__(self):
        return self.recamara_name

class Bano(models.Model):
    bano_name = models.CharField('Nombre:', max_length=50, default="Nombre Mueble Baño")
    imagen = models.ImageField('Imagen:', upload_to='M-Banos/', blank=False, null=False, default="/static/images/logos/Logo.png")
    descripcion = models.CharField('Descripcion:', max_length=256, default="Descripcion Mueble Baño")
    stock = models.IntegerField('Stock:', default=0)
    precio = models.FloatField('Precio:', default=0.00)
    timestamp = models.DateField(auto_now_add=True)
    update_baño = models.DateField(auto_now=True, auto_now_add=False)
    status = models.BooleanField('Estado:', default=True)
    codigo = models.SlugField('Código:', max_length=16)

    def __str__(self):
        return self.bano_name

class Cocina(models.Model):
    cocina_name = models.CharField('Nombre:', max_length=50, default="Nombre Mueble Cocina")
    imagen = models.ImageField('Imagen:', upload_to='M-Cocinas/', blank=False, null=False, default="/static/images/logos/Logo.png")
    descripcion = models.CharField('Descripcion:', max_length=256, default="Descripcion Mueble Cocina")
    stock = models.IntegerField('Stock:', default=0)
    precio = models.FloatField('Precio:', default=0.00)
    timestamp = models.DateField(auto_now_add=True)
    update_cocina = models.DateField(auto_now=True, auto_now_add=False)
    status = models.BooleanField('Estado:', default=True)
    codigo = models.SlugField('Código:', max_length=16)

    def __str__(self):
        return self.cocina_name

class Comedor(models.Model):
    comedor_name = models.CharField('Nombre:', max_length=50, default="Nombre Mueble Comedor")
    imagen = models.ImageField('Imagen:', upload_to='M-Comedores/', blank=False, null=False, default="/static/images/logos/Logo.png")
    descripcion = models.CharField('Descripcion:', max_length=256, default="Descripcion Mueble Comedor")
    stock = models.IntegerField('Stock:', default=0)
    precio = models.FloatField('Precio:', default=0.00)
    timestamp = models.DateField(auto_now_add=True)
    update_comedor = models.DateField(auto_now=True, auto_now_add=False)
    status = models.BooleanField('Estado:', default=True)
    codigo = models.SlugField('Código:', max_length=16)

    def __str__(self):
        return self.comedor_name

class Sala(models.Model):
    sala_name = models.CharField('Nombre:', max_length=50, default="Nombre Mueble Sala")
    imagen = models.ImageField('Imagen:', upload_to='M-Sala/', blank=False, null=False, default="/static/images/logos/Logo.png")
    descripcion = models.CharField('Descripcion:', max_length=256, default="Descripcion Mueble Sala")
    stock = models.IntegerField('Stock:', default=0)
    precio = models.FloatField('Precio:', default=0.00)
    timestamp = models.DateField(auto_now_add=True)
    update_sala = models.DateField(auto_now=True, auto_now_add=False)
    status = models.BooleanField('Estado:', default=True)
    codigo = models.SlugField('Código:', max_length=16)

    def __str__(self):
        return self.sala_name

class Oficina(models.Model):
    oficina_name = models.CharField('Nombre:', max_length=50, default="Nombre Mueble Oficina")
    imagen = models.ImageField('Imagen:', upload_to='M-Oficinas/', blank=False, null=False, default="/static/images/logos/Logo.png")
    descripcion = models.CharField('Descripcion:', max_length=256, default="Descripcion Mueble Oficina")
    stock = models.IntegerField('Stock:', default=0)
    precio = models.FloatField('Precio:', default=0.00)
    timestamp = models.DateField(auto_now_add=True)
    update_oficina = models.DateField(auto_now=True, auto_now_add=False)
    status = models.BooleanField('Estado:', default=True)
    codigo = models.SlugField('Código:', max_length=16)

    def __str__(self):
        return self.oficina_name
