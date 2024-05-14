from django.db import models

class	Colaborator(models.Model):
	id_colaborator = models.AutoField(primary_key=True)
	fname = models.CharField(max_length=100)
	lname = models.CharField(max_length=100)
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	tier = models.IntegerField()
	department = models.CharField(max_length=100)
	role = models.CharField(max_length=100)
	admission_date = models.DateField()
	functional_group = models.CharField(max_length=100)

	def	__str__(self):
		return self.fname + ' ' + self.lname

class	Event(models.Model):
	id_event = models.AutoField(primary_key=True)
	beginning = models.DateField()
	end = models.DateField()
	status = models.BooleanField(default=False)

	def __str__(self):
		return "Evento" + ' ' + self.id_event

class	Evaluation(models.Model):
	id_evaluation = models.AutoField(primary_key=True)
	id_evaluator = models.IntegerField()
	id_evaluated = models.IntegerField()
	id_event = models.IntegerField()
	status = models.BooleanField()

	def __str__(self):
		return "Avaliação" + ' ' + self.id_avaliation

class	Criteria(models.Model):
	id_evaluation = models.IntegerField()
	question = models.CharField(max_length=200)
	answer = models.IntegerField()
	description = models.CharField(max_length=255)
	comment = models.CharField(max_length=255)

	def __str__(self):
		return "Criteria" + ' ' + self.question