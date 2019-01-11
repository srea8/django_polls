# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.views import generic
# from django.template import loader

from .models import Question,Choice
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
		selected_choice = question.choice_set.all()
	except (KeyError,Choice.DoesNotExist):
		return render(request, "polls/detail.html", {'question': question,'error_message':"you did't select a choice."})
	else:
		selected_choice.votes = 0
		selected_choice.save()
	return HttpResponseRedirect(reverse('polls:results',args=(question.id,)))
