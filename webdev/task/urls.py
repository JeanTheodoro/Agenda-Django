from django.urls import path
from .views import home 
from .views import detail
from .views import delete

app_name = 'task'

urlpatterns = [
    path('', home, name='home'),
    path('<int:task_id>', detail, name='detail'),
    path('delete/<int:task_id>', delete, name='delete')
]
