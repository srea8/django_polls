from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns = [
	# url(r'^$', views.index, name='index'),
	# url(r'^(?P<question_id>[0-9]+)/$', views.detail,name='detail'),
	# url(r'^(?P<question_id>[0-9]+)/results/$', views.results,name='results'),
	url(r'^$', views.Indexview.as_view(), name='index'),
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(),name='detail'),
	url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(),name='results'),
	url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote,name='vote'),
	url(r'^(?P<question_id>[0-9]+)/clearvote/$', views.clearvote,name='clearvote'),
	url(r'^newquestion/$', views.newquestion, name='newquestion'),
	url(r'^addquestion/$', views.addquestion, name='addquestion'),
	url(r'^listquestionnaire/$', views.QuestionnaireView.as_view(), name='listquestionnaire'),
	url(r'^(?P<pk>[0-9]+)/questiondetail/$', views.QuestionnaireDetailView.as_view(), name='questiondetail'),
	url(r'^(?P<questionnaire_id>[0-9]+)/questionnairevote/$', views.questionnairevote,name='questionnairevote'),
]
