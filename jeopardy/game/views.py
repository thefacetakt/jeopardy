from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from .models import Question, User, Category, Game

def index(request):
    username = None
    if request.user.is_authenticated():
        username =  request.user.username
    return render(request, 'index.html', {'username': username})

def signIn(request):
    return render(request, 'signin.html')

def signUp(request):
    return render(request, 'signup.html')

@require_POST
def signInProcess(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
    return redirect('/')
            # Redirect to a success page.
        #else:
            # Return a 'disabled account' error message
    #else:
        # Return an 'invalid login' error message.

@login_required
def addQuestionPage(request):
    return render(request, 'addQuestion.html',
        {
            'categories' : Category.objects.all()
        }
    )

@require_POST
def addQuestion(request):
    Question(
        readingTime = float(request.POST['readingTime']),
        answeringTime = float(request.POST['answeringTime']),
        price = int(request.POST['price']),
        statement = request.POST['statement'],
        answer = request.POST['answer'],
        category = Category.objects.get(id=int(request.POST['category'])),
        author = request.user,
    ).save()
    return redirect('/')

@login_required
def myQuestionList(request):
    return render(request, 'myQuestionList.html', 
        { 
            'questions' : Question.objects.filter(author=request.user),
        }
    )

@login_required
def addCategoryPage(request):
    return render(request, 'addCategory.html')

@require_POST
def addCategory(request):
    Category(
        title = request.POST['title'],
    ).save()
    return redirect('/')

@login_required
def addGamePage(request):
    return render(request, 'addGame.html',
        {
            'categories' : Category.objects.all(),
        }
    )

def questionsByCategory(request):
    if (request.is_ajax()):
        questions = Question.objects.filter(category=Category.objects.get(id=int(request.GET['category'])))
        data = serializers.serialize('json', questions)
        return HttpResponse(data, 'application/javascript')
    return HttpResponse(status=400)


@login_required
@require_POST
def registerGame(request):
    game = Game(author=request.user)
    game.save()
    return HttpResponse(game.id, 'application/javascript')

@login_required
@require_POST
def addCategoryToGame(request):
    gameId = int(request.POST["game"]);
    print(gameId);
    print(request.user);
    game = Game.objects.get(id=gameId);
    print(game.author)
    if (game.author == request.user):
        for i in range(100, 501, 100):
            print(request.POST[str(i)])
            print(str(request.POST[str(i)]))
            print(Question._meta.fields)
            game.questions.add(Question.objects.get(id=int(request.POST[str(i)])))
    return HttpResponse(status=200)



