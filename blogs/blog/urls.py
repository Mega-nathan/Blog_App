from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path('',views.home,name='home'),
    path('createBlog',views.CreateBlog.as_view(),name='createBlog'),
    path('blog/<int:id>/',views.detailed_blog,name='detailed_blog'),
    path('viewBlog',views.view_blog,name='viewBlog'),
    path('editBlog/<int:id>/',views.edit_blog,name='editBlog'),
    path('api/blogs/',views.blog_list,name='blog_list'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)