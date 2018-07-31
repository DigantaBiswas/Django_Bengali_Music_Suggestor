from django.db import models
from django.utils import timezone

# Create your models here.
class Music_data(models.Model):
	title = models.CharField(max_length = 200)
	youtube_url = models.CharField(max_length = 500)
	artist = models.CharField(max_length = 50)
	genre = models.CharField(max_length = 50)
	release_date = models.IntegerField()
	created_date = models.DateTimeField(auto_now_add = True)


	def created(self):
		self.created_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title