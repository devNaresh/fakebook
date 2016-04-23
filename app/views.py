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


# Home page of fakebook wall
def home(request):
    if request.user.id is None:  # If user is Anonymous then redirect to SignIn page
        return HttpResponseRedirect(reverse("signIn"))
    posts = Posts.objects.all().order_by("-modified")  # Get Context of Post and pass to template
    context = {"posts": posts,
               "name": request.user.username}
    return render(request, "wall.html", context)


# Render SignUp Page
def signUp(request):
    return render(request, "signUp.html")


# Render SignIn Page
def signIn(request):
    # TODO -: Should be in Sign Up ...Please change
    if request.method == "POST" and request.user.id is None:  # If POST request then create User
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
    elif request.method == "GET" and request.user.id is not None:  # If user Authenticated return True
        return JsonResponse(data={"success": True})
    else:
        return render(request, "signIn.html")


# For Logout, Just LogOut User
def logout(request):
    auth.logout(request)
    response = HttpResponseRedirect(reverse("home"))
    response.set_cookie(key='token', value='')
    return response


# View for Add User in to Database
class UserSignUp(CreateAPIView):
    serializer_class = UserSerializer  # Using User serializer
    parser_classes = (FormParser, JSONParser)


# View for Add Post in to Database
class PostView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = PostSerializer
    parser_classes = (FormParser, JSONParser)


# View for Add Comments in to Database
class CommentView(CreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer
    parser_classes = (FormParser, JSONParser)
