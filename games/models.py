from django.db import models

# Create your models here.
class Game(models.Model):
	Created = models.DateTimeField(auto_now_add=True)
	Name = models.CharField(max_length =200, blank =True, default ='')
	Release_date = models.DateTimeField()
	Game_category = models.CharField(max_length=200,blank=True,default='')
	Played = models.BooleanField(default=False)

	class Meta:
		ordering = ('Name',)