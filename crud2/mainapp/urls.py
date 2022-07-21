from django.urls import path
from . import views

urlpatterns = [
    path('', views.studentList, name = "studentList"),
    path('detail/<int:pk>/', views.studentDetail, name = "studentDetail"),
    path('create', views.studentCreate, name = "studentCreate"),
    path('update/<int:pk>/', views.studentUpdate, name = "studentUpdate"),
    path('delete/<int:pk>/', views.studentDelete, name = "studentDelete")
]

#     path('<int:pk>/', DetailStudent.as_view()),
#     path('', ListStudent.as_view()),
#     path('create', CreateStudent.as_view()),
#     path('delete/<int:pk>', DeleteStudent.as_view())
# ]