from django.db import models

# Create your models here.
class SignUp(models.Model):
	first_name = models.Charfield(max_length=120, null=True, blank=True)
	last_name = models.Charfield(max_length=120, null=True, blank=True)
	email =

