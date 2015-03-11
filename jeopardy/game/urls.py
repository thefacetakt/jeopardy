from django.conf.urls import patterns, url

from game import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url('signin/', views.signIn, name='signin'),
    url('signInProcess/', views.signInProcess, name='signinprocess'),
    url('addQuestion/', views.addQuestionPage, name='addQuestion'),
    url('addQuestionProcess/', views.addQuestion, name='addQuestionProcess'),
    url('myQuestionList/', views.myQuestionList, name='myQuestionList'),
    url('addCategory/', views.addCategoryPage, name='addCategory'),
    url('addCategoryProcess/', views.addCategory, name='addCategoryProcess'),
    url('addGame/', views.addGamePage, name='addGame'),
    url('getQuestions/', views.questionsByCategory, name='getQuestions'),
    
    #url('signup/', views.signUp, name='signup'),
    #url('signupprocess/', views.signUpProcess, name='signupprocess'),
)