from django.urls import path, include
from .views import  TagDetail,TagList,overview,SnippetList,SnippetDetail

urlpatterns = [
    path('snippet', SnippetList.as_view()),
    path('snippet/<int:pk>' , SnippetDetail.as_view()),
    path('Tag', TagList.as_view(), name ='TagList'),
    path('Tag/<int:pk>', TagDetail.as_view()),
    path('', overview),
    # path('TagList/',TagList.as_view(), name ='TagList'),
]
