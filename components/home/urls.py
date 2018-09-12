from django.conf.urls import url, include
from components.login import views as loginviews
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
urlpatterns = [
    path('', LoginView.as_view(template_name='login.html', extra_context={next: 'asdf.html'}), name='login')
    #path('', loginviews.index)
    ]