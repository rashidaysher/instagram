
from django.contrib import admin
from django.urls import path,include
from . import  views
from django.contrib.staticfiles.urls import static
from . import settings
import os
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django.contrib.auth.urls')),
    path('',include('insta.urls')),
    path('signup/',views.signup,name="signup"),

] +static(settings.MEDIA_URL,document_root=os.path.join(settings.BASE_DIR,'media'))
