from django.urls import path

from models_demo.web import views

urlpatterns = (
    path("", views.info, name='info'),
    path("departments/", views.show_all_departments, name="departments"),
    path("delete/<int:pk>/", views.delete_employee, name="delete employee"),
)
