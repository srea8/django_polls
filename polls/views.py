# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views import generic
# from django.template import loader

from .models import Question,Choice,Questionnaire
# Create your views here.


# def index(request):
# 	latest_question_list = Question.objects.order_by('-pubdate')[:5]
# 	# 第一种方法
# 	# template = loader.get_template('polls/index.html')
# 	# context = {'latest_question_list':latest_question_list,}
# 	# return HttpResponse(template.render(context,request))
	
# 	# django的第二种方法
# 	context = {'latest_question_list':latest_question_list,}
# 	return render(request,"polls/index.html", context)


# def detail(request, question_id):
# 	# 第一种方法
#     # try:
#     #     question = Question.objects.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
# 	#django的第二种方法
# 	question = get_object_or_404(Question, pk = question_id)
# 	return render(request, "polls/detail.html", {'question': question})

# def results(request, question_id):
# 	question = get_object_or_404(Question, pk = question_id)
# 	return render(request, "polls/results.html", {'question': question})

class Indexview(generic.ListView):
	"""docstring for Indexview"""
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'
	def get_queryset(self):
		return Question.objects.all()[:5]
		

class DetailView(generic.DetailView):
	"""docstring for DetailView"""
	model = Question
	template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
	"""docstring for DetailView"""
	model = Question
	template_name = 'polls/results.html'


def vote(request, question_id):
	question = get_object_or_404(Question,pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError,Choice.DoesNotExist):
		return render(request, "polls/detail.html", {'question': question,'error_message':"you did't select a choice."})
	else:
		selected_choice.votes += 1
		selected_choice.save()
	return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))


def clearvote(request, question_id):
	question = get_object_or_404(Question,pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError,Choice.DoesNotExist):
		selected_choices = question.choice_set.all()
		for selected_choice in selected_choices:
			selected_choice.votes = 0
			selected_choice.save()
	else:
		selected_choice.votes = 0
		selected_choice.save()

	return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))

def newquestion(request):
	"""docstring for DetailView"""
	return render(request, "polls/newquestion.html", {})

def addquestion(request):
	if request.method == 'POST':
		addquestion=request.POST.get("question",None)
		currenttime=request.POST.get("currenttime",None)
		choicevalues = request.POST.getlist("choicevalues",None)
		if addquestion!=None and currenttime!=None:
			newquestion = Question()
			newquestion.question_text = addquestion
			newquestion.pubdate = currenttime
			newquestion.save()
			A = Question.objects.get(question_text=newquestion)
			for choicevalue in choicevalues:
				choices = Choice()
				choices.question=A
				choices.choice_text = choicevalue
				choices.votes = 0
				choices.save()

		return HttpResponseRedirect(reverse('polls:index',args=()))
	return HttpResponseRedirect(reverse('polls:newquestion',args=()))


class QuestionnaireView(generic.ListView):
	template_name = 'polls/listquestionnaire.html'
	context_object_name = "questionnaire_list"
	def get_queryset(self):
		return Questionnaire.objects.all()


class QuestionnaireDetailView(generic.DetailView):
	"""docstring for DetailView"""
	model = Questionnaire
	template_name = 'polls/questiondetail.html'


def questionnairevote(request, questionnaire_id):
	questionnaire = get_object_or_404(Questionnaire,pk=questionnaire_id)
	#print questionnaire.id
	for question in questionnaire.members.all():
		try:
			selected_choice = question.choice_set.get(pk=request.POST.get('choice'))
			print str(request.POST.get('choice'))
		except (KeyError,Choice.DoesNotExist):
			return render(request, "polls/questiondetail.html", {'questionnaire': questionnaire,'error_message':"you did't select a choice."})
		else:
			selected_choice.votes += 1
			selected_choice.save()
	return HttpResponseRedirect(reverse('polls:index',args=()))