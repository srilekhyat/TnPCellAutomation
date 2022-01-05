"""tnpcellautomation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from user.views import home_view, prof_register_view, student_register_view, register_view, prof_register_view, profile_view, search_users
from opportunities.views import display, add_opportunity, add_to_interests, edit_opportunity, delete_opportunity, remove_from_interests
from stats.views import get_data, show_stats, show_total
from learningmaterial.views import learning_material_home, topic_info, topics_view, add_concept, delete_concept, edit_concept, add_topic, edit_topic, delete_topic
from qa.views import add_answer, qa_home, add_question, display_answers

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name="home"),
    path('search/', search_users, name="search"),

    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
    path('register/', register_view, name="register"),
    path('studentregistration/', student_register_view, name="stud_register"),
    path('profregistration/', prof_register_view, name="prof_register"),
    
    path(r'^profile/(?P<username>\w+)/$', profile_view, name="profile"),
    
    path('opportunities/', display, name="display"),
    path('addopp/', add_opportunity, name="add-ops"),
    path(r'^deleteopp/(?P<id>\d+)/$', delete_opportunity, name="delete-ops"),
    path(r'^editopp/(?P<id>\d+)/$', edit_opportunity, name="edit-opp"),

    path(r'^addtointerests/(?P<id>\d+)/$', add_to_interests, name="addtointerests"),
    path(r'^removefrominterests/(?P<id>\d+)/$', remove_from_interests, name="removefrominterests"),
    
    path('stats/', show_stats, name="stats_page"),
    path('showchart/', get_data, name="showchart"),
    
    path('learningmaterial/', learning_material_home, name="lrng_mtrl"),
    path(r'^editlm/(?P<id>\d+)/$', edit_concept, name="edit-lm"),
    path(r'^deletelm/(?P<id>\d+)/$', delete_concept, name="delete-lm"),
    path(r'^lmtopics/(?P<id>\d+)/$', topics_view, name="lm-topics"),
    path(r'^lminfo/(?P<id>\d+)/$', topic_info, name="lm-info"),
    path('addconcept/', add_concept, name="add_concept"),
    path(r'^addtopic/(?P<id>\d+)/$', add_topic, name="add-topics"),
    path(r'^edittopic/(?P<id>\d+)/$', edit_topic, name="edit-topic"),
    path(r'^deletetopic/(?P<id>\d+)/$', delete_topic, name="delete-topic"),

    path('qa/', qa_home, name="qa"),
    path('add_qa/', add_question, name="add_qa"),
    path(r'^add_answer/(?P<id>\d+)/$', add_answer, name="add_ans"),
    path(r'^show_answer/(?P<id>\d+)/$', display_answers, name="show_ans"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
