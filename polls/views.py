from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
# Create your views here.

def index(request):
    # result = ""
    # for q in Question.objects.raw('SELECT * FROM polls_question'):
    #     result += str(q) + " <br> "
    # rows = Question.objects.raw('SELECT question_text, id FROM polls_question WHERE id=1')
    rows = Question.fetch_all()

    output = rows[0]['question_text'] + "<br>" +  rows[1]['question_text'] + "<br><br>Γεια σας αυτή θα είναι η αρχική σελίδα της εφαρμογής Polls! <br><a href='myview'> go </a>"

    return HttpResponse(output)

def myview(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', <br>'.join([q.question_text for q in latest_question_list])
    output += "<br><br> Αυτή είναι μία δεύτερη σελίδα. <br><a href='home'> back </a>"
    return HttpResponse(output)

    # response = "You're looking at the results of question %s." +
    # return HttpResponse(response % question_id)


