from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import Question

'''#index estático simplis
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
'''

'''#segunda forma do index
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', <br>'.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)
'''

'''#index interativo primeira parte
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))
'''

#reescrita do index interativo
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

'''#reescrita da view datail
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'polls/detail.html',{'quesyion':question})
'''

#forma mais simplificada de levantar um erro 404 (Django)
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)

