urlpatterns = [
    path('', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
]
