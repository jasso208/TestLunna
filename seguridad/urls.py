from django.conf.urls import url
from seguridad.apis.apis import *
from seguridad.apis.UserApi import UserApi

app_name = "seguridad"

urlpatterns=[
	url(r'^api_login_front/$',api_login_front,name = "api_login_front"),
	url(r'^user/$',UserApi.as_view()),
]

