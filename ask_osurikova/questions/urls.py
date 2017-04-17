from django.conf.urls import url
from questions.views import about,\
    list_of_questions,\
    hot_questions,\
    question, questions_of_tag,\
    log_in, sign_up,\
    ask,\
    settings


urlpatterns = [
    url(r'^$', list_of_questions, name='list_of_questions'),
    url(r'^hot/$', hot_questions, name='hot_questions'),
    url(r'^question/(?P<id>\d+)/$', question, name='question'),
    url(r'^tag/(?P<tag>\w+)/$', questions_of_tag, name='tag'),
    url(r'^login/$', log_in, name='log_in'),
    url(r'^signup/$', sign_up, name='sign_up'),
    url(r'^ask/$', ask, name='ask'),
    url(r'^settings/$', settings, name='settings'),
    url(r'^about$', about, name='about'),
]
