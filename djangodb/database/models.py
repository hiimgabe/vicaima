# pylint: disable=missing-class-docstring

from django.db import models
from django.contrib.auth.models import User
from django.db.models import signals
from django.dispatch import receiver

class Colaborator(models.Model):
    id_colaborator = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    admission_date = models.DateField()
    functional_group = models.CharField(max_length=100)

    def	__str__(self):
        return self.fname + ' ' + self.lname

class Event(models.Model):
    id_event = models.AutoField(primary_key=True)
    beginning = models.DateField()
    end = models.DateField()
    status = models.BooleanField(default=False)
    evaluated = models.ManyToManyField(Colaborator, related_name='evaluated_events')

    def status_as_string(self):
        return 'Finished' if self.status else 'Ongoing'

    def __str__(self):
        return "Evento" + ' ' + str(self.id_event)

class	Evaluation(models.Model):
    id_evaluation = models.PositiveIntegerField(primary_key=True)
    id_evaluator = models.ForeignKey(Colaborator, on_delete=models.CASCADE, related_name='evaluations_as_evaluator')
    id_evaluated = models.ForeignKey(Colaborator, on_delete=models.CASCADE, related_name='evaluations_as_evaluated')
    id_event = models.ForeignKey(Event, on_delete=models.CASCADE, db_column='id_event')
    status = models.BooleanField()

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
