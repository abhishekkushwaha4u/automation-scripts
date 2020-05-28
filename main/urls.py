from django.urls import path
from . import views

urlpatterns = [
    path('script/', views.ScriptListCreateAPIView.as_view()),
    path('script/<pk>/', views.ScriptRetrieveUpdateDestroyAPIView.as_view()),
    path('search/script/byName/', views.ScriptRetrieveByNameView.as_view()),
    path('search/script/byNumber/', views.ScriptRetrieveByNoOfRecords.as_view()),
]