
from django.urls import path

from .views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', index, name='index'),
    path('biz', BizViews.as_view()),
    path('blog', BlogViews.as_view()),
    # path('video', VideoViews.as_view()),
    path('blog/<int:id>',blog_detail),
    

]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)