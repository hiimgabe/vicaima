# pylint: disable=missing-class-docstring

from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from django.core.exceptions import ObjectDoesNotExist


class Colaborator(models.Model):
	id_colaborator = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	num_colaborator = models.IntegerField()
	fname = models.CharField(max_length=100)
	lname = models.CharField(max_length=100)
	username = models.CharField(max_length=100)
	department = models.CharField(max_length=100)
	role = models.CharField(max_length=100)
	admission_date = models.DateField()
	functional_group = models.CharField(max_length=100)

	def	__str__(self):
		return self.fname + ' ' + self.lname

def get_default_evaluator():
	try:
		return Colaborator.objects.get(id_colaborator=1).id_colaborator.id # type: ignore
	except ObjectDoesNotExist:
		return None# type: ignore

class Event(models.Model):
	NORMAL_EVALUATION = 'NE'
	EVALUATION_WITH_AUTOEVALUATION = 'EA'
	FULL_360_EVALUATION = 'F3'

	TYPE_OF_EVALUATION_CHOICES = [
		(NORMAL_EVALUATION, 'Normal'),
		(EVALUATION_WITH_AUTOEVALUATION, 'Normal + Auto-Evaluation'),
		(FULL_360_EVALUATION, 'Full 360'),
	]

	id_event = models.AutoField(primary_key=True)
	begin_event = models.DateField()
	end_event = models.DateField()
	status = models.BooleanField(default=False)
	evaluated = models.ManyToManyField(Colaborator, related_name='evaluated_events')
	evaluator = models.ForeignKey('database.Colaborator', on_delete=models.CASCADE, default=get_default_evaluator, related_name='evaluator_events')
	type_of_evaluation = models.CharField(max_length=2, choices=TYPE_OF_EVALUATION_CHOICES, default=NORMAL_EVALUATION)

	def status_as_string(self):
		return 'Finished' if self.status else 'Ongoing'

	def __str__(self):
		return "Evento" + ' ' + str(self.id_event)

	def save(self, *args, **kwargs):
		is_new = self.pk is None
		super().save(*args, **kwargs) 
		if is_new: # Call the "real" save() method.
			self.create_evaluations()

	def create_evaluations(self):
		for colaborator in self.evaluated.all():
			Evaluation.objects.create(
				id_evaluator=self.evaluator,
				id_evaluated=colaborator,
				id_event=self,
				status='NS',
			)

@receiver(m2m_changed, sender=Event.evaluated.through)
def create_evaluations(sender, instance, action, **kwargs):
	if action == "post_add":
		instance.create_evaluations()

class	Evaluation(models.Model):
	NOT_STARTED = 'NS'
	ONGOING = 'OG'
	DONE = 'DN'

	STATUS_CHOICES = [
		(NOT_STARTED, 'Not Started'),
		(ONGOING, 'Ongoing'),
		(DONE, 'Done'),
	]

	id_evaluation = models.AutoField(primary_key=True)
	id_evaluator = models.ForeignKey(Colaborator, on_delete=models.CASCADE, related_name='evaluations_as_evaluator')
	id_evaluated = models.ForeignKey(Colaborator, on_delete=models.CASCADE, related_name='evaluations_as_evaluated')
	id_event = models.ForeignKey(Event, on_delete=models.CASCADE, db_column='id_event')
	status = models.CharField(
		max_length=2,
		choices=STATUS_CHOICES,
		default=NOT_STARTED,
	)

	def __str__(self):
		return "Avaliação" + ' ' + str(self.id_evaluation)

class Criteria(models.Model):
	id_evaluation = models.ForeignKey(Evaluation, on_delete=models.CASCADE, db_column='id_evaluation')
	question = models.CharField(max_length=200)
	answer = models.PositiveIntegerField()
	description = models.CharField(max_length=255)
	comment = models.CharField(max_length=255, default="Nada a acrescentar")

	def __str__(self):
		return self.question
