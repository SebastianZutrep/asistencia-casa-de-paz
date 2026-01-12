from django.db import models
from datetime import date


# Create your models here.

class Integrante(models.Model):

    SEXO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Femenino'),
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    tipo = models.CharField(
        max_length=10,
        choices=[('niño', 'Niño'), ('joven', 'Joven'), ('servidor', 'Servidor')]
    )
    telefono = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    ultima_asistencia = models.DateField(null=True, blank=True)
    descripcion = models.TextField(blank=True, null=True)
    activo = models.BooleanField(default=True)
    rol = models.CharField(
        max_length=10,
        choices=[('Maestro', 'Maestro'), ('Lider', 'Líder')],
        null=True,
        blank=True
    )

    direccion = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    sexo = models.CharField(
        max_length=1,
        choices=SEXO_CHOICES,
        blank=True,
        null=True
    )

    @property
    def edad(self):
        if not self.fecha_nacimiento:
            return None

        hoy = date.today()
        return (
            hoy.year - self.fecha_nacimiento.year
            - ((hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day))
        )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
    foto = models.ImageField(
        upload_to='integrantes/',
        blank=True,
        null=True,
        default='integrantes/user_default.png'
    )
    

class Reunion(models.Model):
    TIPO_REUNION = (
        ('J', 'Jovenes'),
        ('N', 'Niños y preadolescentes'),
    )
    fecha = models.DateField()
    tema = models.CharField(max_length=255)
    maestro = models.ForeignKey(
        Integrante,
        on_delete=models.SET_NULL,
        null=True,
        related_name='reuniones_dirigidas'
    )
    tipo = models.CharField(max_length=1, choices=TIPO_REUNION, default='J')

    def __str__(self):
        return f"Reunión {self.fecha} - {self.tema} - {self.get_tipo_display()}"


class Asistencia(models.Model):
    integrante = models.ForeignKey(Integrante, on_delete=models.CASCADE)
    reunion = models.ForeignKey(Reunion, on_delete=models.CASCADE)
    presente = models.BooleanField(default=False)
    comentario = models.TextField(null=True, blank=True)

    class Meta:
        unique_together = ('integrante', 'reunion')  # PK compuesta

    def __str__(self):
        estado = "Asistió" if self.presente else "No asistió"
        return f"{self.integrante} - {self.reunion}: {estado}"



    
