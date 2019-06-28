from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class Task(models.Model):
	name = models.CharField(max_length=100, null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	due = models.DateTimeField(null=True, blank=True)
	assignee = models.ForeignKey(User, related_name='Assigned_To', on_delete=models.CASCADE,null=True, blank=True)
	assigner = models.ForeignKey(User, related_name='Assigned_By', on_delete=models.CASCADE,null=True, blank=True)
	STATUSES = (
		('TD', "To Do"),
		('D', "Done"),
		)
	status = models.CharField(max_length=100, choices=STATUSES, default='TD')
	parent = models.ForeignKey('Task', related_name='Parent', on_delete=models.CASCADE, null=True, blank=True)

	def __str__(self):
		return self.name
	
	def get_absolute_url(self):
		return reverse('task-detail', kwargs={'pk': self.pk})

