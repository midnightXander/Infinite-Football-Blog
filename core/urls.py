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
    path('edit_post/<int:post_id>',views.edit_post,name="edit_post"),
    path('<str:category_name>',views.category,name='category'),
    path('<str:category_name>/<int:post_id>',views.post,name="post"),
    
    

]