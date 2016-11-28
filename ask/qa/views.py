from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.decorators.http import require_GET

from qa.models import Question
from qa.utils.viewhelpers import paginate
# Create your views here.

def test(request, *args, **kwargs):
    return HttpResponse('OK')

@require_GET
def home(request):
    questions = Question.objects.new()
    paginator, page = paginate(request, questions)
    paginator.baseurl = '/?page='
    return render(request, 'home.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })


@require_GET
def popular(request):
    questions = Question.objects.popular()
    paginator, page = paginate(request, questions)
    paginator.baseurl = '/popular/?page='
    return render(request, 'home.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
})
