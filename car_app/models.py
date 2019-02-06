from django.db import models
from django.utils import timezone


class TruckModel(models.Model):
	model_name = models.CharField(max_length=20, unique=True)
	max_capacity = models.IntegerField(default=0)
	model_description = models.TextField(max_length=1000, 
			help_text='Enter a brief description of the Truck Model', blank=True, null=True)
			
	class Meta:
		verbose_name = 'TruckModel'
		verbose_name_plural = 'TruckModels'
		
		
	def __str__(self):
		return self.model_name


class TruckNumber(models.Model):
	bort_number = models.CharField(max_length=20, unique=True)
	model_name = models.ForeignKey(TruckModel, on_delete=models.SET_NULL, null=True)
	truck_number_description = models.TextField(max_length=1000, 
			help_text='Enter a brief description of the Truck Number', blank=True, null=True)
	
	current_weight = models.IntegerField(default=0)
		
	registration_date = models.DateTimeField(
			default=timezone.now)
	current_work_start_date = models.DateTimeField(
			blank=True, null=True)
	overload = models.FloatField(default=0)
	
	class Meta:
		verbose_name = 'TruckNumber'
		verbose_name_plural = 'TruckNumbers'
		
	def __str__(self):
		return str(self.bort_number)
		


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title
        
        
        