from django.urls import path
# from app.views import index
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns =[
    path("",views.index,name='index'),
    path("home/",views.home,name="home"),
    # path("",views.myfile)

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 