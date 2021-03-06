from django.urls import path

from oth import views

app_name = 'oth'
urlpatterns = [
    path('', views.index, name='index'),
    path('answer/<int:pk>', views.answer, name='answer'),
    path('lboard/', views.lboard, name='lboard'),
    path('rules/', views.rules, name='rules'),
    path('finish/', views.finish, name='finish'),
    path('attachment/<int:pk>', views.view_video, name='attachment'),
    path('stay_tuned/', views.stay_tuned, name='stay_tuned'),
    path('video_feed', views.video_feed, name='video_feed'),
    path('not_happy', views.not_happy, name='not_happy'),

]
