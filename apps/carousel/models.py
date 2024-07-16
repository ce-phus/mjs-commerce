from django.db import models

class CarouselItem(models.Model):
	id = models.AutoField(primary_key=True)
	title = models.CharField(max_length=255)
	image_url = models.URLField()
	description = models.TextField()
	image_field = models.ImageField(upload_to='uploads/', blank=True, null=True)

	
    

	def __str__(self):
		return self.title
