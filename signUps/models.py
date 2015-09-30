from django.db import models

# Create your models here.
class SignUp(models.Model):
	first_name = models.Charfield(max_length=120, null=True, blank=True)
	last_name = models.Charfield(max_length=120, null=True, blank=True)
	email = models.EmailField()

	#add a time stamp
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	#add an updated stamp
	timestamp = models.DateTimeField(auto_now_add=False, auto_now=True)

	#add a unicode function that takes 1 parameter
	def __unicode__(slef):
		self.email
