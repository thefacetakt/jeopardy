from django.conf.urls import patterns, url

from game import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^signin/$', views.signIn, name='signin'),
    url(r'^signInProcess/$', views.signInProcess, name='signinprocess'),
    url(r'^addQuestion/$', views.addQuestionPage, name='addQuestion'),
    url(r'^addQuestionProcess/$', views.addQuestion, name='addQuestionProcess'),
    url(r'^myQuestionList/$', views.myQuestionList, name='myQuestionList'),
    url(r'^addCategory/$', views.addCategoryPage, name='addCategory'),
    url(r'^addCategoryProcess/$', views.addCategory, name='addCategoryProcess'),
    url(r'^addGame/$', views.addGamePage, name='addGame'),
    url(r'^getQuestions/$', views.questionsByCategory, name='getQuestions'),
    url(r'^registerGame/$', views.registerGame, name='registerGame'),
    url(r'^addCategoryToGame/$', views.addCategoryToGame, name='addCategoryToGame'),
    url(r'^game/(?P<game_id>\d+)/$', views.gameProcess, name='gameProcess'),
    url(r'^addPlayerToGame/$', views.addPlayerToGame, name='addPlayerToGame'),
    url(r'^removePlayerFromGame/$', views.removePlayerFromGame, name='removePlayerFromGame'),
    #url('signup/', views.signUp, name='signup'),
    #url('signupprocess/', views.signUpProcess, name='signupprocess'),
)