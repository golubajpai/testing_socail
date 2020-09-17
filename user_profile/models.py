from django.db import models
from .manager import *
from django.contrib.auth.models import AbstractUser
from common_utils.constants import *






class User(AbstractUser):
	
	username = None
	email = models.EmailField(unique=True)
	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = []
	objects = UserManager()



	class Meta:
		db_table = 'user_table'



	def __str__(self):
		return self.email +" "+str(self.id)






class User_Interest(models.Model):
	topic=models.CharField(max_length=100)



	def save(self, *args, **kwargs):
		self.topic='#'+self.topic
		return super(User_Interest, self).save(*args, **kwargs)

	class Meta:
			db_table = 'user_interest'

	def __str__(self):
		return str(self.id)




class Profile(models.Model):
	user_id=models.OneToOneField(User,on_delete=models.CASCADE)
	profile_pic=models.ImageField(null=True,blank=True)
	about=models.TextField()
	full_name = models.CharField(max_length=200, null=True, blank=True)
	interest=models.ManyToManyField(User_Interest)
	class Meta:
			db_table = 'profile'












class Follow(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	user_follow=models.ForeignKey(User,related_name='user_followers',on_delete=models.CASCADE)

	class Meta:
		unique_together = ('user', 'user_follow',)



class Posts(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	post_text=models.TextField()














