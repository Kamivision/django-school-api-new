from django.urls import path
from .views import AllSubjects, SubjectView

urlpatterns = [
    path('', AllSubjects.as_view(), name='all_subjects'),
    path('<str:name>/', SubjectView.as_view(), name='a_subject'),
]

