# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

class Question(models.Model):
	question_text = models.CharField(max_length=200)
	pubdate = models.DateTimeField('date published')

	def was_published_recently(self):
		return self.pubdate>=timezone.now()-datetime.timedelta(days=1)

	def __unicode__(self):
		return self.question_text

class Choice(models.Model):
	question = models.ForeignKey(Question,on_delete = models.CASCADE)
	choice_text = models.CharField(max_length=200)
	votes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.choice_text

