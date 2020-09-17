from common_utils.constants import  *

from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.contrib.auth import  login
from datetime import datetime, timezone
from rest_framework import exceptions

from .models import *
from django.contrib.auth import authenticate
from rest_framework.exceptions import PermissionDenied
from rest_framework import validators 
User=get_user_model()



class UserSerializer(serializers.ModelSerializer):
	password = serializers.CharField(write_only = True)
	
	class Meta:
		model=User
		fields='__all__'


	def create(self,validated_data):
		user=super(UserSerializer,self).create(validated_data)
		user.set_password(validated_data['password'])
		user.save()
		return user






class User_login_sere(serializers.Serializer):
	email=serializers.EmailField()
	password= serializers.CharField(write_only=True)

	def validate(self,data):
		if data.get('email')!=None and data.get('password')!=None:
			user=authenticate(email=data.get('email'),password=data.get('password'))
			if user:
				return user

			else:
				raise  PermissionDenied(INVALID_EMAIL_CREDENTIALS)


		else:
			raise  ValueError(REQUIRED_CREDENTIALS )





class CreateProfileSere(serializers.ModelSerializer):

	def __init__(self, *args, **kwargs):
		super(CreateProfileSere, self).__init__(*args, **kwargs)
		for validator in self.fields['user_id'].validators:
			if isinstance(validator, validators.UniqueValidator):
				validator.message = (ALREADY_PROFILE)
	class Meta:
		model=Profile
		fields='__all__'
		#depth=1



	def to_representation(self,instance):
		data=super(CreateProfileSere,self).to_representation(instance)
		data=data.copy()
		data.update(UserSerializer(instance.user_id).data)
		data.pop('interest')
		data['interest']=UserInterestSere(instance.interest.all(),many=True).data
		return data





class UserInterestSere(serializers.ModelSerializer):
	class Meta:
		model=User_Interest
		fields='__all__'




class FollowSere(serializers.ModelSerializer):




	class Meta:
		model=Follow
		fields='__all__'
		validators = [
			serializers.UniqueTogetherValidator(
			queryset=model.objects.all(),
			fields=('user', 'user_follow'),
			message=(ALREADY_FOLLOW)
			)
			]






	def to_representation(self,instance):
		data=super(FollowSere,self).to_representation(instance)
		data.pop('user')

		try:

			return {'you_are_following':CreateProfileSere(instance.user_follow.profile).data}

		except:
			return {'you_are_following':UserSerializer(instance.user_follow).data}





class PostSere(serializers.ModelSerializer):
	user_data=UserSerializer(source='user' ,required=False)


	class Meta:
		model=Posts
		fields= '__all__'























	





		
