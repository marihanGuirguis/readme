from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index ,name='home'),
    path('login', auth_views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout',auth_views.logout,{'next_page':'login'},name='logout'),
    path('books/<which>/ajax/favourite/', views.favourite, name='addFav'),
    path('books/<which>/ajax/rate/', views.rate, name="rate"),
    path('books/<which>/ajax/read/', views.read, name="read"),
    path('books/<which>/ajax/wishlist/', views.wishlist, name="wishlist"),
    path('authers/<who>/ajax/follow/', views.follow, name="authfollow"),
    path('templates/ajax/getcategory/', views.getcategory, name="getcategory"),
    path('templates/ajax/get_author/', views.get_author, name="get_author"),
    path('templates/ajax/get_book/', views.get_book, name="get_book"),
    path('books/<which>/', views.which_book, name='which_book'),
    path('authers/<who>/', views.who_author, name='who_author'),
    path('<type>/', views.categoryPage, name='categoryPage'),
    path('<type>/ajax/Categoryfollow/', views.categoryFollow, name='categoryFollow'),
    path('search/<token>', views.searchPg, name='searchPg'),
    path('allAuthors', views.get_all_author, name='get_all_author'),
    path('profile', views.profile, name='profile'),
    path('updateUser', views.updateUser, name='updateUser'),
    path('updateUserPassword',views.changePasswordUser,name='changePasswordUser'),


]
