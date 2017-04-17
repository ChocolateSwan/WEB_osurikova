from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from questions.data import *
from questions.pagination import paginate
from questions.models import *

# Create your views here.


@csrf_exempt
def about(request):
    data = []
    if request.method == 'GET':
        data = request.GET
    if request.method == 'POST':
        data = request.POST
    return render(request, 'about.html',
                  {'method': request.method,
                   'data': data})


def right_column(request):
    return ({
        'authors': authors,
        'tags': tags,
    })


def list_of_questions(request):
    q = Question.objects.all()
    paginated_questions, paginator, page_range = paginate(q, request)
    return render(request, 'list_of_questions.html',
                  {'page': paginated_questions,
                   'pageRange': page_range,
                   'right_column': right_column(request),
                   'head': 'Questions'})


def hot_questions(request):
    paginated_hot_questions, paginator, page_range = paginate(questions, request)
    return render(request, 'list_of_questions.html',
                  {'page': paginated_hot_questions,
                   'pageRange': page_range,
                   'right_column': right_column(request),
                   'head': 'Hot Questions'})


def questions_of_tag(request, tag):
    paginated_tag_questions, paginator, page_range = paginate(questions, request)
    return render(request, 'list_of_questions.html',
                  {'page': paginated_tag_questions,
                   'pageRange': page_range,
                   'right_column': right_column(request),
                   'head': 'Tag: ' + tag})


def question(request, id):
    q = questions[int(id)-1] if int(id)<len(questions) else ({
        'title': 'title ' + str(id),
        'id': id,
        'text': 'text ' + str(id),
        'answers': id,
    })
    return render(request, 'question.html',
                  {'question': q,
                   'right_column': right_column(request),
                   'answers': answers})


def log_in(request):
    return render(request, 'log_in.html',
                  {'right_column': right_column(request)})
    # return render(request, 'form.html',{'form': form, 'head': head, 'right_column': right_column(request),'button': button})


def sign_up(request):
    return render(request, 'sign_up.html',
                  {'right_column': right_column(request)})


def ask(request):
    return render(request, 'new_question.html',
                  {'right_column': right_column(request)})


def settings(request):
    return render(request, 'settings.html',
                  {'right_column': right_column(request)})