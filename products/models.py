from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):

	title = models.CharField(max_length=200)
	pub_date = models.DateTimeField()
	body = models.TextField()
	url = models.URLField(max_length=200)
	image = models.ImageField(upload_to="img/")
	icon = models.ImageField(upload_to="img/")
	votes_total = models.IntegerField(default=1)
	hunter = models.ForeignKey(User, on_delete=models.CASCADE)

	#change title name in admin page to be title
	def __str__(self):
		return self.title
	
	def summary(self):
		return self.body[:200]

	# simplify date output converting to
	def pub_date_pretty(self):
			return self.pub_date.strftime('%b %e %Y') #just yr,date,mo