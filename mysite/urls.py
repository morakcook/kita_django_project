"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('single_pages.urls')),
    path('blog/', include('blog.urls')),
    path('markdownx/', include('markdownx.urls')),
    path('accounts/', include('allauth.urls')), # 별도의 인증 관련 URL 및 뷰를 직접 구현할 필요 없이, django-allauth가 제공하는 기능을 쉽게 이용
    path('data/', include('data.urls')),
]

urlpatterns += static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    # 미디어 파일을 서빙할 수 있도록 urlpatterns에 추가
)
