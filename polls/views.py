from django.shortcuts import get_object_or_404, render

from .models import Question, Choice

from django.http import Http404

# Create your views here.
def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list': latest_question_list}
	return render(request, 'polls/index.html', context)


def detail(request, question_id):
	try:
		question = Question.objects.get(pk=question_id)
	except Question.DoesNotExist:
		raise Http404('Question does not exist.')
	else:
		return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
	return HttpResponse('These are the results of the question %s' % question_id)


def vote(request, question_id):
	return HttpResponse('Vote on question: %s' % question_id)


def info(request, question_id):
	return HttpResponse('Here is some info on: %s' % question_id)