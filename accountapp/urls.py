from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp"

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),# name은 route가 너무 길어지게 되면 앱 이름을 통해 바로 접근할 수 있도록 하는 역할

    path('create/',AccountCreateView.as_view(),name='create')
]