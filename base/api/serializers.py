from rest_framework.serializers import  ModelSerializer
from base.models import  Post,Profile,Company
from django.contrib.auth.models import User


class  PostSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'

class  UserSerializer(ModelSerializer):

    class Meta:
        model=User
        fields=['id','username','email']
        
class ProfileSerializer(ModelSerializer):
    user=UserSerializer(many=False)
    class Meta:
        model=Profile
        fields='__all__'

class CompanySerializer(ModelSerializer):
    class Meta:
        model=Company
        fields='__all__'