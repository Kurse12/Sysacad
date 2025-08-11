from django.db import models

# Create your models here.
from usuarios.models import Usuario
from materias.models import Materia

class Inscripcion(models.Model):
    alumno = models.ForeignKey(Usuario, on_delete=models.CASCADE, limit_choices_to={'rol': 'alumno'})
    materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    estado = models.CharField(max_length=20, choices=[
        ('inscripto', 'Inscripto'),
        ('cursando', 'Cursando'),
        ('aprobado', 'Aprobado'),
        ('desaprobado', 'Desaprobado'),
    ])
    
    def __str__(self):
        return f'Inscripcion {self.id}: {self.alumno}, {self.materia}, {self.fecha}, {self.estado}'
