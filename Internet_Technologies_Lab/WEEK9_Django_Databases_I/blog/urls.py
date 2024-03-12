from django.urls import include,path 
from blog.views import archive,create_blogpost 

urlpatterns = [ 
    path(r'', archive, name='archive'), 
    path(r'create/', create_blogpost, name='create_blogpost'), 
 ] 
