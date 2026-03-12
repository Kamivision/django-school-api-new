from django.urls import path
from .views import AllStudentsView, StudentView


urlpatterns = [
    path('', AllStudentsView.as_view(), name='all_students'),
    path('<int:id>/', StudentView.as_view(), name='a_student'),
]
