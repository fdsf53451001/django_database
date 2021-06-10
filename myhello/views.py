from django.core import paginator
from django.db.models.lookups import PostgresOperatorLookup
from django.shortcuts import render
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
from django.core.paginator import Page, Paginator,EmptyPage,PageNotAnInteger

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import json

from .models import Post
# from .models import User

# Create your views here.

class HelloAPIView(APIView):
    def get(self,request):
        get_name = request.GET.get('name',None)
        # logger.debug("**************** HelloAPIView : "+get_name)
        retValue = {}
        if get_name:
            retValue['data'] = "Hello " + get_name
            return Response(retValue,status=status.HTTP_200_OK)
        else:
            retValue['data'] = None
            return Response(retValue,status=status.HTTP_400_BAD_REQUEST)

class Add_post(APIView):
    def get(self,request):
        title = request.GET.get('title','')
        content = request.GET.get('content','')
        photo = request.GET.get('photo','')
        location = request.GET.get('location','')

        new_post = Post()
        new_post.title = title
        new_post.content = content
        new_post.photo = photo
        new_post.location = location
        new_post.save()

        if title:
            return JsonResponse({'data':title + 'insert!'},status=status.HTTP_200_OK)
        else:
            return JsonResponse({'res':'parameter : name is None'},status=status.HTTP_400_BAD_REQUEST)
        
class List_post(APIView):
    def get(self,request):
        page = request.GET.get('page',1) #  browsing page i
        posts = Post.objects.all().values()

        paginator = Paginator(posts,10) #10 data for one page
        try:
            posts = paginator.page(page)
        except PageNotAnInteger:
            posts = paginator.page(1)
        except EmptyPage:
            posts = paginator.page(paginator.num_pages)

        return JsonResponse(
            # {'data':json.dumps(list(posts),sort_keys=True,indent=1,cls=DjangoJSONEncoder)},
            {'data':list(posts)},
            status=status.HTTP_200_OK
        )


# class List_user(APIView):
#     def get(self,request):
#         users = User.objects.all().values()
#         return JsonResponse(
#             {'data':json.dumps(list(users),sort_keys=True,indent=1,cls=DjangoJSONEncoder)},
#             status=status.HTTP_200_OK
#         )