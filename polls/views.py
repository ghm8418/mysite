from django.shortcuts import render
from django.http import HttpResponse
from polls.models import Question

# Create your views here.

# def index(request):
#     q = Question.objects.all()[0]
#     choices = q.choice_set.all()
#
#     print(q.question_text)
#     print(choices[0].choice_text)
#     print(choices[1].choice_text)
#     print(choices[2].choice_text)
#
#     return HttpResponse('polls index')
def index(request):
    questions = Question.objects.all()
    return render(request,
                  'polls/index.html',
                  {'question': questions })

def detail(request, question_id): # 질문 상세 페이지
    q = Question.objects.get(id=question_id)
    c = q.choice_set.all()
    choice = ''
    for a in c:
        choice += a.choice_text
    #             request  '템플릿'  {컨텍스트(데이터/모델)}
    return render(request,
                  'polls/detail.html',
                  {'question' : q.question_text,
                   'num': q.id,
                  'choice' : c})
    #return HttpResponse(q.question_text + '<br>' + choice)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id): # 투표 페이지
    q = Question.objects.get(id=question_id)
    try:
        select = request.POST['select']
        c = q.choice_set.get(id=select)
        c.votes += 1
        c.save()
        print(select)
    except:
        pass

    return render(request,
                  'polls/result.html',
                  {'q':q}
    )

def detail2(request, num1, num2): #덧셈
    return HttpResponse(num1 + num2)

def edit(request, question_id):
    q = Question.objects.get(id = question_id)

    return render(request, 'polls/edit.html', {'q' : q} )

def save(request, question_id):
    q = request.POST['q']
    question = Question.objects.get(id=question_id)
    question.question_text = q
    question.save()

    return HttpResponse('수정완료')