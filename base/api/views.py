from rest_framework.response import Response
from rest_framework.decorators import api_view
from
@api_view(['GET'])
def  getRoutes(request):
    routes={
        'users':'api/users',
        'posts':'api/posts'
    }
    return  Response()