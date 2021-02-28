from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    # #/polls/
    # path('', views.index, name='index'),
    # #/polls/question_id
    # path('<int:question_id>/', views.detail, name='detail'),
    # #/polls/question_id/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # #/polls/question_id/results/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]