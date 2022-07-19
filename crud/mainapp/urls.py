from django.urls import path
from .views import *

urlpatterns = [
    path('<int:pk>/', DetailStudent.as_view()),
    path('', ListStudent.as_view()),
    path('create', CreateStudent.as_view()),
    path('delete/<int:pk>', DeleteStudent.as_view())
]