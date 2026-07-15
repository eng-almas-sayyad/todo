from django.urls import path
from . import views

urlpatterns = [
    path('addTask/',views.addTask,name='addTask'),
    path('markCompleted/',views.markCompleted,name = 'markCompleted'),
    path('deleteTask/<int:pk>',views.deleteTask,name='deleteTask'),
    path('restoreTask/<int:pk>',views.restoreTask,name = 'restoreTask'),
    path('editTask/',views.editTask,name = 'editTask'),
]