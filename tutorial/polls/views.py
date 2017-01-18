from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_boy('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    return HttpResponse("You're looking at question {}.".format(question_id))


def results(request, question_id):
    response = "You're looking at the results of question {}".format(question_id)
    return HttpResponse(response)


def vote(request, question_id):
    return HttpResponse("You're voting on question {}".format(question_id))