from django.urls import path
from . import views

app_name = 'Books'
urlpatterns = [
    # /Books/
    path('', views.index, name='index'),
    # /Books/id e.g. /Books/1
    path('<int:Books_id>/', views.show, name='show'),
    path('<int:book_id>/save_feedback/', views.save_feedback, name='save_feedback'),
    path('<int:feedback_id>/delete_feedback/', views.delete_feedback, name='delete_feedback'),
    path('<int:feedback_id>/update_feedback/', views.update_feedback, name='update_feedback'),
]
