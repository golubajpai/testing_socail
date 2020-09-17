from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializer import  *
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from common_utils.pagination import  MediumPagination
from django.db.models import Q
from rest_framework import status
from common_utils.permissions import  SuperuserOrGetOnly

# Create your views here.


class CreateUser(APIView):

	def post(self,request):
		user_data=UserSerializer(data=request.data)
		user_data.is_valid(raise_exception=True)
		user_data.save()
		return Response({'data':user_data.data},status=status.HTTP_201_CREATED)



class Login(APIView):
	def post(self,request):
		login_data=User_login_sere(data=request.data)
		login_data.is_valid(raise_exception=True)
		token, _ = Token.objects.get_or_create(user=login_data._validated_data)
		return Response({'token':token.key})





class CreateProfile(ModelViewSet):
	permission_classes=(IsAuthenticated,)
	serializer_class=CreateProfileSere
	permission_classes=(IsAuthenticated,)



	def get_serializer_context(self):
		context = super(CreateProfile, self).get_serializer_context()
		context.update({"request": self.request})
		return context

	def create(self,request):
		request.data._mutable = True
		request.data['user_id']=request.user.id
		request.data._mutable = False
		return super(CreateProfile,self).create(request)





	def get_queryset(self,request):

		return Profile.objects.filter(user_id=self.request.user)




class Mutual_interst(APIView):
	permission_classes=(IsAuthenticated,)
	def get(self,request):
		'''to get the profile who have same intrest'''

		profile= Profile.objects.filter(~Q(user_id=request.user),interest__in=request.user.profile.interest.all())
		return Response({'data':CreateProfileSere(profile,many=True).data})





class InterestList(ModelViewSet):
	pagination_class=MediumPagination
	permission_classes=(SuperuserOrGetOnly,)
	serializer_class=UserInterestSere
	queryset=User_Interest.objects.all()




class Follow_Unfollow(ModelViewSet):
	serializer_class=FollowSere
	permission_classes=(IsAuthenticated,)


	def create(self,request):
		'''follow'''
		request.POST._mutable = True
		request.data['user']=request.user.id
		request.POST._mutable = False
		return super(Follow_Unfollow,self).create(request)


	def get_queryset(self):
		
		follow_object=Follow.objects.filter(user=self.request.user)
			
		return follow_object


	def destroy(self,request,*args,**kwargs):
		instance=self.get_object()

		'''un follow users'''

		if instance.user==request.user:
			self.perform_destroy(instance)
			return Response({'delete':'success'})
		return Response({'error':'dont have permissions'})




class PostsView(APIView):
	permission_classes=(IsAuthenticated,)
	def post(self,request):
		request.POST._mutable = True
		request.data['user']=request.user.id
		request.POST._mutable = False

		post_data=PostSere(data=request.data)
		post_data.is_valid(raise_exception=True)
		post_data.save()
		return Response({'data':post_data.data})


	def get(self,request):

		'''raw query so user see the post whom they are following '''
		post_queryset=Posts.objects.raw('select * from user_profile_posts inner join '
			'user_profile_follow on user_profile_follow.user_follow_id=user_profile_posts.user_id '
			'where user_profile_follow.user_id={} ;'.format(request.user.id))

		

		post_json=PostSere(post_queryset,many=True)
		return Response(post_json.data)


 




















	


