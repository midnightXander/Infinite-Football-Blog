from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('',views.index,name='index'),
    
    path('login',views.login_view,name='login'),
    path('logout',views.logout_view,name='logout'),
    path('register',views.register,name='register'),
    path('add_post',views.add_post,name="add_post"),
    
    path('matches',views.matches,name='matches'),
    path('matches/<int:match_id>',views.match_details,name="match_details"),
    path('matches/<int:match_id>/alt-links',views.alt_links,name="alt_links"),
    path('edit_post/<int:post_id>',views.edit_post,name="edit_post"),
    path('<str:category_name>',views.category,name='category'),
    path('<str:category_name>/<int:post_id>',views.post,name="post"),
    
    

]