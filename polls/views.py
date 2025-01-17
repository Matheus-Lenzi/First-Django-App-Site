from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from django.views import generic
from django.utils import timezone
import matplotlib.pyplot as plt
import io
import urllib, base64
from .models import Question, Choice

# def index(request):
#     latest_question_list = Question.objects.order_by('-pub_date')[:5]
#     # template = loader.get_template('polls/index.html')
#     # context = {
#     #     'latest_question_list': latest_question_list,
#     # }
#     # output = ', '.join([q.question_text for q in latest_question_list])
#     # return HttpResponse(output)
#     # return HttpResponse(template.render(context, request))
#     return render(request, 'polls/index.html', context = {'latest_question_list': latest_question_list,})

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        # return Question.objects.order_by('-pub_date')[:5]
        return Question.objects.filter(pub_date=timezone.now()).order_by('-pub_date')[:5]

# def detail(request, question_id):
#     # try:
#     #     question = Question.object.get(pk=question_id)
#     # except Question.DoesNotExist:
#     #     raise Http404("Question does not exist")
#     # return HttpResponse("You're looking at question's %s." % question_id)
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {'question': question})

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'
    def get_queryset(self):
        return Question.objects.filter(pub_date=timezone.now())

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     # plt.plot(range(10))
#     # fig = plt.gcf()
#     # buf = io.BytesIO()
#     # fig.savefig(buf, format='png')
#     # buf.seek(0)
#     # string = base64.b64encode(buf.read())
#     # uri = urllib.parse.quote(string)
#     # return render(request, 'polls/result.html', {'question': question, 'data': uri})
#     return render(request, 'polls/results.html', {'question': question})

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except(KeyError, Choice.DoesNotExist):
        return render( request, 'polls/detail.html', {'question': question, 'error_message': "You didn't select a choice",})
    else:
        selected_choice.votes = selected_choice.votes + 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question_id, )))
    # return HttpResponse("You're voting on question %s." % question_id) 
