from django.conf.urls import include, url
urlpatterns = [

    url(r'^controle/',include('controle.urls',namespace='controle_v1')),


]
urlpatterns += [

    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),

]


