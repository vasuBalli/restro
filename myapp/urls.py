from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about.html',views.about,name="about"),
    path('service.html',views.service,name="service"),
    path('menu.html',views.menu,name="menu"),
    path('booking.html',views.booking,name="booking"),
    path('testimonial.html',views.testimonial,name="pages"),
    path('contact.html',views.contact,name="contact"),
    path('team.html',views.team,name="team")
]