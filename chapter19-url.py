from django.urls import path #type: ignore
from . import views

urlpatterns = [
    # Page for adding a new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]