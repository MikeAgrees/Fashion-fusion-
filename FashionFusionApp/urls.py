from django.urls import path
from FashionFusionApp import views 
urlpatterns =[
    path('',views.index, name='index'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout, name='logout'),
    path('addToCart/',views.addToCart, name='addToCart'),
    path('checkout/',views.checkout, name='checkout'),
    path('shopping-cart/', views.shoppingCart, name='shopping-cart'),
    path('remove-from-cart/', views.removeFromCart, name='removeFromCart'),
    path('updateCart/',views.updateCart,name='updateCart'),

    path("about-us/", views.about_us, name="about"),
    path("shop-details/", views.shop_details, name="shop_details"),
    path("blog-details/", views.blog_details, name="blog_details"),
    path("blog/", views.blog, name="blog"),
    path("contact/", views.contact, name="contact"),

    #crude operation urls
    path('crud_view/',views.crud_view,name='crud_view'),
    path('add/',views.add,name='add'),
    path('update/',views.update,name='update'),
    path('delete/',views.delete,name='delete'),
    path('edit/',views.edit,name="edit"),
    path('delete-inline/',views.delete_inline,name="delete-inline"),
]