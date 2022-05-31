from django.db import models

class Mug(models.Model):
	nickname = models.CharField(max_length=50)
	image = models.ImageField(upload_to='images/')
	officialName = models.CharField(max_length=50, blank=True, null=True)
	figures = models.ManyToManyField('Figure', blank=True, null=True)
	colors = models.ManyToManyField('Color', blank=True, null=True)
	theme = models.ForeignKey('Theme', on_delete=models.CASCADE, blank=True, null=True)

	def __str__(self):
		return self.nickname

	def get_absolute_url(self):
		return f"/moominmugs/{self.pk}"

class Figure(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return f"/figures/{self.pk}"

class Color(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return f"/colors/{self.pk}"

class Theme(models.Model):
	name = models.CharField(max_length=20)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return f"/themes/{self.pk}"
