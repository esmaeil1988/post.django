
from django.contrib import admin
from django.urls import path
from dent.views import *
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('contact/', contact),
    path('register/', register),


    path('showdr/<adad>', showdr),
    path('shownews/<adad>', shownews),
]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)