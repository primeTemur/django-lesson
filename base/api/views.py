from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Post,Profile,Company
from .serializers import PostSerializer,UserSerializer,ProfileSerializer,CompanySerializer
from django.contrib.auth.models import  User


@api_view(['GET'])
def  getRoutes(request):
    routes={
        'users':'api/users',
        'posts':'api/posts'
    }
    return  Response(routes)

@api_view(['GET'])
def getPosts(request):
    posts=Post.objects.all()
    serializers=PostSerializer(posts,many=True)
    return Response(serializers.data)


@api_view(['GET'])
def getPost(request,pk):
    post=Post.objects.get(id=pk)
    serializers=PostSerializer(post,many=False)
    return Response(serializers.data)


@api_view(['GET'])
def getUsers(request):
    users=Profile.objects.all()
    serializers=ProfileSerializer(users,many=True)
    return Response(serializers.data)

@api_view(['GET'])
def getUser(request,username):
    user=Profile.objects.get(user__username=username)
    serializers=ProfileSerializer(user,many=False)
    return Response(serializers.data)

@api_view(['GET'])
def getCompanies(request):
    serializers=CompanySerializer(Company.objects.all(),many=True)
    return Response(serializers.data)