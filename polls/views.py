# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404,render
from django.http import HttpResponse
# from django.template import loader

from .models import Question
# Create your views here.

def index(request):
	latest_question_list = Question.objects.order_by('-pubdate')[:5]
	# 第一种方法
	# template = loader.get_template('polls/index.html')
	# context = {'latest_question_list':latest_question_list,}
	# return HttpResponse(template.render(context,request))
	
	# django的第二种方法
	context = {'latest_question_list':latest_question_list,}
	return render(request,"polls/index.html", context)


def detail(request, question_id):
	# 第一种方法
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404("Question does not exist")
	#django的第二种方法
	question = get_object_or_404(Question, pk = question_id)
	return render(request, "polls/detail.html", {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)