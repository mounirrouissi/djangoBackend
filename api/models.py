# Create your models here.
from django.db import models


class Reservation(models.Model):
	   # Country Choices

	PLACES_CHOICES = (
		('1', '1'),
		('2', '2')
	)
	CATEGORY_CHOICES = (
	('enfant', 'enfant'),
	('adult', 'adult'),
    ('etudiant', 'etudiant'),
    
	)
	places=models.CharField(max_length=15, choices=PLACES_CHOICES,default=0)
	category=models.CharField(max_length=15, choices=CATEGORY_CHOICES,default="")
	name = models.CharField(max_length=32)
	city = models.CharField(max_length=256,default="")
 
class Festival(models.Model):
    	   # Country Choices


	name=models.CharField(max_length=15,default="")
	status=models.CharField(max_length=15,default="")
	city = models.CharField(max_length=32,default="")
