from django.db import models
from datetime import datetime

class Evento(models.Model):
    titolo = models.CharField(max_length=100)
    descrizione = models.TextField
    data_inizio = models.DateField(default=datetime.now(), blank=True)
    data_fine = models.DateField(default=datetime.now(), blank=True)
    posti_disponibili = models.IntegerField(blank=True, default=0)
    
    def __str__(self):
        return self.titolo
    
    class Meta:
        verbose_name = "Evento"
        verbose_name_plural = "Eventi"
