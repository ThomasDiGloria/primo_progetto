from django.db import models
from datetime import datetime

class Corso(models.Model):
    titolo = models.CharField(100)
    descrizione = models.TextField
    data_inizio = models.DateField(default=datetime.now(), blank=True)
    data_fine = models.DateField(default=datetime.now(), blank=True)
    posti_disponibili = models.IntegerField(blank=True, default=0)
    
    def __str__(self):
        return self.titolo + " " + self.descrizione + " " + self.data_inizio + " " + self.data_fine + " " + self.posti_disponibili
    
    '''class Meta:
        verbose_name = "Giornalista"
        verbose_name_plural = "Giornalisti"
        '''
