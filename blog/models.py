from django.db import models
#importowanie daty i czasu
from django.utils import timezone
# Create your models here.

class Post(models.Model):
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	title = models.CharField(max_length=200)
	text   = models.TextField()
	create_date = models.DateTimeField(default = timezone.now)
	publish_date = models.DateTimeField(blank = True, null = True)
	# null oznacza że można wypęłnić takie pole kiedy indziej.

	#nazwa jest dowolna
	def publish(self):
		self.publish_date = timezone.now()
		self.save()
		#donder -> double under score
	def __str__(self):
		return self.title



