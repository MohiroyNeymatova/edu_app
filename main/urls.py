from django.urls import path
from .views import *

urlpatterns = [
    path('student_create/', student_create),
    path('direction_create/', direction_create),
    path('get_directions/', get_directions),
    path('group_create/', group_create),
    path('students_get/', students_get),
    path('groups_get/', groups_get),
    path('payment_create/', payment_create),
    path('get_group_by_id/<int:pk>', get_group_by_id),
    path('payed_students/', payed_students),
    path('get_waiting_students/', get_waiting_students),
    path('get_quantity_of_students/', get_quantity_of_students),
    path('get_groups_name/', get_groups_name)
]