from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from base.models import Post,Profile,Company,JobOpening
from .serializers import PostSerializer,UserSerializer,ProfileSerializer,CompanySerializer,JobOpeningSerializer
from django.contrib.auth.models import  User
from rest_framework.permissions import IsAuthenticated,IsAdminUser

@api_view(['GET'])
def  getRoutes(request):
    routes={
        'users':'api/users',
        'user object':'api/users/<username>',
        'posts':'api/posts',
        'post object':'api/posts/<pk>',
        'post add':'api/posts/add/<pk>',
        'post update':'api/posts/edit/<pk>',
        'post delete':'api/posts/delete/<pk>',
    }
    return  Response(routes)

@api_view(['GET'])
def getPosts(request):
    posts=Post.objects.all()
    serializers=PostSerializer(posts,many=True)
    return Response(serializers.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def addtPosts(request):
    data=request.data
    user=request.user
    post=Post.objects.create(
        owmer=user,
        body=data['body']
    )
    serializer=PostSerializer(post,many=False)

    return Response({   
        'message':'Post Added!',
        'data':serializer.data
    })

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def editPost(request,pk):
    data=request.data
    user=request.user
    post=Post.objects.get(id=pk)
    if user == post.owmer:
        post.body=data['body']
        post.save()

        serializer=PostSerializer(post,many=False)

        return Response({   
            'message':'Post Update!',
            'data':serializer.data
        })
    else:
        return Response({'message':'You can not edit this post!'})

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def deletePost(request,pk):
    post=Post.objects.get(id=pk)
    user=request.user
    if user==post.owmer:
        post.delete()
        return Response('Post Deleted!')
    else:
        return Response('You can not delete this post!')

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
def getRecommendedUsers(request):
    users=Profile.objects.filter(verified=True).order_by('?')
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


@api_view(['GET'])
def getCompany(request,pk):
    serializers=CompanySerializer(Company.objects.get(id=pk),many=False)
    return Response(serializers.data)

@api_view(['GET'])
def getLatestJobs(request):
    jobs=JobOpening.objects.all().order_by('-created')[0:10]
    serializers=JobOpeningSerializer(jobs,many=True)
    return Response(serializers.data)