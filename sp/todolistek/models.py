from django.db import models

#from django 

class Uporabnik(models.Model):
	U_ime = models.CharField(max_length=50)
	U_email = models.CharField(max_length=250)
	
	def __str__(self):
		return self.U_ime + ' ' + self.U_email

class Opravilo(models.Model):
	O_uporabnik = models.ForeignKey(Uporabnik, on_delete=models.CASCADE)
	O_ime = models.CharField(max_length=50)
	O_kategorija = models.CharField(max_length=50)
	O_casovna_zahtevnost = models.CharField(max_length=50)
	O_opraviti_do = models.CharField(max_length=50)
	O_pomembnost = models.CharField(max_length=50)
	O_opis = models.CharField(max_length=1000, null=True)
	
	def __str__(self):
		return self.O_ime