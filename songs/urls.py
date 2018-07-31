from django.conf.urls import url
from django.views.generic import TemplateView
from .import views


urlpatterns = [
	url(r'^$',views.home, name = 'home_url'),
	url(r'^suggestion/$',views.suggestion, name ='suggestion_url')
	# url(r'^home', 
 #    TemplateView.as_view(template_name='songs/musicSuggestion.html'),
 #    name='home'),

]