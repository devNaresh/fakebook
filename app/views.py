from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.parsers import FormParser, JSONParser
from rest_framework.permissions import IsAuthenticated

from .models import Posts
from .serializer import PostSerializer, CommentSerializer, UserSerializer


# Create your views here.

def home(request):
    if request.user.id is None:
        return HttpResponseRedirect(reverse("signIn"))
    posts = Posts.objects.all().order_by("-modified")
    context = {"posts": posts,
               "name": request.user.username}
    return render(request, "wall.html", context)


def signUp(request):
    return render(request, "signUp.html")


def signIn(request):
    if request.method == "POST" and request.user.id is None:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return JsonResponse(data={"success": True})
            else:
                return JsonResponse(data={"error": "wrong username and password"})
        else:
            return JsonResponse(data={"error": "wrong username and password"})
    elif request.method == "GET" and request.user.id is not None:
        return JsonResponse(data={"success": True})
    else:
        return render(request, "signIn.html")


def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect(reverse("home"))
    response.set_cookie(key='token', value='')
    return response


class UserSignUp(CreateAPIView):
    serializer_class = UserSerializer
    parser_classes = (FormParser, JSONParser)


class PostView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    parser_classes = (FormParser, JSONParser)


class CommentView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer
    parser_classes = (FormParser, JSONParser)
