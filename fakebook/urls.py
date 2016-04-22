from django.conf.urls import patterns, include, url
from django.contrib import admin
from app import views
urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^post/', views.PostView.as_view(), name='post'),
    url(r'^comment/', views.CommentView.as_view(), name='postComment'),
    url(r'^signUp/', views.signUp, name='signUp'),
    url(r'^signIn/', views.signIn, name='signIn'),
    url(r'^addUser/', views.UserSignUp.as_view(), name='addUser'),
    url(r'^logout/', views.logout, name='signOut'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
