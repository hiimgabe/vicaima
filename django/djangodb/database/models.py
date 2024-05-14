from django.db import models

class	User(models.Model):
	id = models.AutoField(primary_key=True)
	fname = models.CharField(max_length=100)
	lname = models.CharField(max_length=100)
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	email = models.EmailField(max_length=254)
	contact = models.CharField(max_length=100)
	tier = models.CharField(max_length=100)
	functgroup = models.CharField(max_length=100)
	department = models.CharField(max_length=100)
	role = models.CharField(max_length=100)
	admissiondate = models.DateField(max_length=100)

	def	__str__(self):
		return self.fname + ' ' + self.lname