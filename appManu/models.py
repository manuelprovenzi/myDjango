from django.db import models 


# Create your models here.
class Telefono(models.Model):
    name = models.CharField(max_length=255)
    schermo=models.CharField(max_length=255)
    def __str__(self):
        return self.name
    
class Libro(models.Model):
    id = models.CharField(max_length=255, primary_key = True)
    autore =models.CharField(max_length=255, null=True)
    titolo =models.CharField(max_length=255, null=True)
    genere =models.CharField(max_length=255, null=True)
    prezzo =models.FloatField(null=True)
    data_pubblicazione =models.CharField(max_length=255, null=True)
    descrizione = models.CharField(max_length=255, null=True)
    
    def parse(self,attributes):
        for value in attributes.items():
            attributo = value[1]
            nome = value[0]
            
            match nome:
                case "id":
                    self.id = attributo
                case "autore":
                    self.autore = attributo    
                case "titolo":
                    self.titolo = attributo
                case "genere":
                    self.genere = attributo
                case "prezzo":
                    self.prezzo = attributo
                case "data_pubblicazione":
                    self.data_pubblicazione = attributo
                case "descrizione":
                    self.descrizione = attributo   
                    
                    
class Cd(models.Model):
    id = models.CharField(max_length=255, primary_key = True)
    titolo =models.CharField(max_length=255, null=True)
    artista =models.CharField(max_length=255, null=True)
    nazione =models.CharField(max_length=255, null=True)
    azienda =models.CharField(max_length=255, null=True)
    prezzo =models.FloatField(null=True)
    anno = models.CharField(max_length=255, null=True)
    
    def parse(self,attributes):
        for value in attributes.items():
            attributo = value[1]
            nome = value[0]
            
            match nome:
                case "id":
                    self.id = attributo 
                case "TITOLO":
                    self.titolo = attributo
                case "ARTISTA":
                    self.artista = attributo    
                case "NAZIONE":
                    self.nazione = attributo
                case "AZIENDA":
                    self.azienda = attributo
                case "PREZZO":
                    self.prezzo = attributo
                case "ANNO":
                    self.anno = attributo
                