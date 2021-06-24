from django.conf.urls import url
from inventario.apis.ProductosApi import ProductosApi,ProductosListApi
app_name = "inventario"

urlpatterns=[
	url(r'producto/$',ProductosApi.as_view()),
	url(r'producto/(?P<sku>\w+)/(?P<token>\w+)/$',ProductosListApi.as_view()),

    
]
