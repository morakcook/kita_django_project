Model(CRUD)
- 클래스 객체로 데이터에 대한 처리를 한다.
- class로 해서 만들어줘야한다.

ORM(Object-Realational-Mapping)
- Model과 DB의 처리방식의 차이를 해결해주는 방식

Template(화면: hmtl, js, Css)[프론트 엔드]
- 화면을 모아두는 곳
- 프론트엔드하는것처럼 만들면된다.


Tempalte Rendering()
- 화면을 불러들이는 것

템플릿 태그는 파이썬을 HTML로 바꿔주어, 빠르고 쉽게 동적인 웹 사이트를 만들 수 있게한다.
extends : 템플릿 상속
• load : 빌트인 템플릿태그/필터 외에 추가 로딩
• 각 장고앱의 templatetags/ 디렉토리 내, 파일명을 지정
(django/contrib/humanize/tempaltetags/humanize.py)
include : 템플릿 가져오기
• 현재의 context가 그대로 전달.
• with옵션을 통해 추가 키워드 인자 전달
• only 추가옵션을 통해 지정
block … endblock : 블락 영역 지정
• 템플릿 상속을 위한 영역 지정
comment … endcomment : 주석 영역 지정

URLCONF(처리하는 것을 지정?)
- 요청하는 것에 대해 view로직을 연결해야함
- url.py로

View
- url에대해 처리하는 로직이 들어가야함
- view.py
- 해당 솔루션에 대한 api를 view에 넣어야 한다,
- 분석하는 결과를 보여줘야 하는 것이면 view로직을 짜줘야 한다.


-- 설치방법
-requirement.txt로 한꺼번에 설치
- 변경시 requirement.txt를 만들어서 한꺼번에 설치할수도 있음

-- django버전이 중요 최신버전에 대한 교제 없음
-- version: 3으로

cmd :
- cmd에서 안보인다:
		-시스템 환경 변수 편집에서 추가해야함

-------------------------------------------------------------------------
1. 사용하고자 하는 파이썬 확인및 설치
2. 사용하고자 하는 편집기(vscode)에서 확인 where python
3. 확인할때 없을시 path설정, 있을시 진행
3-1. 사용하고자 하는 파이썬을 명시해야함(안그럴시 엉뚱한 파이썬을 사용하게됨)
4. 가상환경 설치
5. requr
-------------------------------------------------------------------------


1. vscode로
2. 가상환경 만들어야하는데 (python버전 확인해야함)
- myenv라는 가상환경 설치하고

1. ctrl+shift+p
2.python 3.10다운 (진행)
3. vscode에 python extention 설치
4. 해당 폴더의 terminal에서 
- C:\Users\SYW\AppData\Local\Programs\Python\Python310\python.exe -m venv myenv
- 안될경우 경로 확인
- 경로에 
	- C:\Users\SYW\AppData\Local\Programs\Python\Python310\Scripts\
	- C:\Users\SYW\AppData\Local\Programs\Python\Python310\
추가

-- 가상환경 설치 끝

5. djangoclass에 requirements.txt 설치
6. requirements.txt 에 필요한 것? 입력
7. 가상환경에 들어가야함
- myenv\Scripts\activate
	- myenv에 scripts에 acivate를 실행
	- 가상환경 실행
8. pip list(설치목록)
9. 입력시 To update, run: 여기있는것 복사해서 실행
10. pip install -r requirements.txt 로 필요한 라이브러리 설치
11. pip list로 확인
12. django-admin startproject mysite . (mysite라는 django프로젝트 생성)



#### django_class 폴더 생성
#### 가상환경을 생성
 - w: python -m venv myenv
 - L: python3 -m venv myenv
#### 생성된 가상환경을 활성화
 - w: myenv\Scripts\activate
 - L: source myenv\bin\activate
#### requirements.txt 생성 및 설치
 - pip install -r requirements.txt
#### 장고 프로젝트 생성
 - django-admin startproject mysite .

#### settings.py 확인(장고 설정)
 - 프로젝트에 대한 설정
 - DEBUG = True : 개발에서는 디버그허용, 실 서버에서는 허용X
 - ALLOWED_HOSTS = [] : 실배포할때 호스트
 - INSTALLED_APPS = [ ] : 앱을 만들때 추가해줘야함
 - ROOT_URLCONF = 'mysite.urls' : urlconf
 - WSGI_APPLICATION = 'mysite.wsgi.application' : django 와 db간의 연결
 - DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
} : 기본으로 sqlite 여기다가 db세팅
- LANGUAGE_CODE = 'en-us' : 언어설정
- TIME_ZONE = 'UTC' : 
- STATIC_URL = '/static/' : 이미지등 정적 요소들의 저장 장소

#### urls.py 확인
- urlpatterns = [
    path('admin/', admin.site.urls),
] : 장고 contirbute에서 admin연결 - 기본 admin이 들어오면 admin.site.urls 매핑

#### manage.py 확인
- def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv) 
        - 장고 명령 실행시 필요

- if __name__ == '__main__':
    main()
    - 이게 참이면 실행 즉 임포트시 실행 방지

#### 기본 실행시
- python manage.py %%%%


#### 서버 관리자 필요 관리자 계정 생성
- python manage.py createsuperuser 
    - username : admin
    - password : admin
    - [y/n] : y
    - 생성됨

#### DB생성
- python manage.py migrate : db생성
    - sqlite라는 DB가 생성된것


#### 서버 실행
- python manage.py runserver
- Starting development server at http://127.0.0.1:8000/ : http://127.0.0.1:8000/가 내 local서버 ctrl+click
- http://127.0.0.1:8000/admin : 관리자 접속
    - id, pw : admin입력 접속 시 관리자 페이지 접속 완료
    - url을 보면 http://127.0.0.1:8000/admin/ 
- 서버 정지키 : ctrl + c

#### app 설치
- python manage.py startapp blog : blog라는 app 설치
- app 등록
    - INSTALLED_APPS = [] 에 'blog', 넣어서 등록(설치)

#### single_pages 기본설정
- from django.urls import path, include : include 를 import해야함
- urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('single_pages.urls')),
]
- single_pages에 urls.py 생성
    - 아무것도 없으면 single_pages에 urls에서 처리하게
    - urls.py 에 
        from django.urls import path
        from . import views

        urlpatterns = [
            path("about_me/", views.about_me),
            path("", views.landing),
]
        입력
            - path, views import
            - 아무것도 없으면 views.landing하고
            - about_me로 들어오면 views.about_me로 처리

- views.py 에 
        def landing(request):
            return render(request, "single_pages/landing.html")
        - 로 landing처리

- single_pages 에 templates/single_pages생성
    - landing.html생성

- 서버실행시
    - 아무것도 없음으로 landing.html 실행됨

정리
    - 서버실행시 아무것도 없으면 을 urls.py에서 정의(views.py에서 처리하게) -> views.py에서 처리 변수? 정의후 처리(return)
    - tempaltes생성(html도 생성) request->urls.py->views.py->templates로 진행



#### 구조
- mysite가 전체 설정




#### 필요 라이브러리 txt생성
- pip install -r requirements.txt

#### 장고 프로젝트 생성
django-admin startproject mysite .

#### 원리
1. 웹클라이언트가 url입력
2. urls.py(urlconf)에 들어가서 urlpattern에서 먼저 작용
3. single_pages.urls.py에 작동
4. single_pages.views.py에 작동(render : 랜더링해라)
5. templates.single_pages.landing.html작동

#### install한것
1. python (extention)
2. Django

#### 앱 생성
- python manage.py startapp blog
- python manage.py startapp single_pages
- settings.py 에 blog앱과 single_pages 앱 등록

#### URLConf
- "URL Configuration"의 약어로, 웹 애플리케이션의 URL, 패턴을 정의하고 관리하는데 사요오디는 중요한 구성 요소

#### templates
 - static :  mysite - settings.py - STATIC_URL = '/static/'
    - {% load static %} : static을 load할때 사용
    - {% %} : Django template문법
    - {%if 조건 %}......{% endif %} : if조건을 쓰면 endif 꼭 필요







장고(Django) 템플릿 시스템은 Python의 웹 프레임워크인 Django의 핵심 부분 중 하나. 이 시스템은 동적 웹 페이지의 내용을 보다 쉽게 생성할 수 있게 해준다. 

1. 템플릿과 컨텍스트
- 템플릿(Template): HTML 파일에 Python 코드와 비슷한 태그를 포함하여 동적인 웹 페이지를 구성.
- 컨텍스트(Context): 템플릿에 전달되는 데이터로, 보통 Python 딕셔너리 형태. 템플릿 태그들은 이 데이터를 활용하여 최종 HTML을 생성.
2. 템플릿 태그
- 변수 출력: {{ variable }} 형태로 사용되며, 컨텍스트에서 해당 변수의 값을 출력.
- 제어 구조: {% if %}, {% for %} 등의 태그를 사용하여 조건문과 반복문을 구현할 수 있다.
    - 예: {% if user.is_authenticated %} Hello, {{ user.username }}! {% endif %}
- 템플릿 상속: {% extends 'base.html' %}를 사용하여 기본 템플릿을 상속받을 수 있다.
    - 블록 태그: {% block content %}{% endblock %}와 같은 형태로, 상속된 템플릿에서 재정의할 수 있는 영역을 지정.
3. 필터
- 변수 변형: {{ variable|filter }} 형태로 사용되며, 변수의 출력 형태를 변경.
- 예: {{ text|lower }}는 text 변수를 소문자로 출력.




## Generic view
- 장고(Django)의 제네릭 뷰(Generic Views)는 일반적인 웹 개발 작업을 위한 미리 정의된 뷰 클래스들을 제공
- 제네릭 뷰를 사용하면 표준적인 CRUD(Create, Read, Update, Delete) 작업을 처리하는 데 필요한 코드 양을 크게 줄일 수 있다.

#### ListView
- 목적: 모델의 객체 목록을 표시하기 위한 뷰
- 특징: 지정된 모델의 모든 레코드(또는 쿼리셋을 통해 필터링된 레코드)를 가져와서 템플릿에 전달
- Django는 클래스 기반 뷰에 대한 기본 템플릿 이름을 자동으로 생성합니다. 이 이름은 {app_name}/{model_name}_list.html 형식을 따릅니다. 예를 들어, Book 모델을 가진 library 앱에 대한 ListView를 생성한다고 가정하면 library/templates/library/book_list.html

#### DetailView 
- 목적: 특정 객체의 상세 정보를 표시하기 위한 뷰. 특징: URL에서 전달된 키(보통 기본 키)를 기반으로 특정 모델 인스턴스를 검색하여 템플릿에 전달. 
- Book 모델에 대한 DetailView를 구현하면 book_detail.html 파일을 생성.
library/templates/library/book_detail.html

#### blog 작업
- urls, view, models, admin, templates 작업
- admin계정 확인
    - add: post추가

- 변경사항 DB 반영시(commit 개념 : 안하면 DB에서 관여할수 없다.)
    - python manage.py makemigrations : 관련 생성자 Create
    - python manage.py migrate : 관련 업데이트 Update

- CBV, FBV
    - FBV : Function Base View
    - CBV : Class Base View
        - generic view : django에서 미리 만들어둔 형식으로 맞춰서 사용가능

#### template모듈화

- include 사용법
    - {% include "base.html" %}을 이용하여 적용할 html에 base.html을 삽입하는 개념이다.

- extends 사용법
    - base.html(불러올 html)
    - page.html(적용할 html)
    - base.html에서 {% block @@@ %}....{% endblock %} : @@@은 id값 같은것임 - 으로 범위를 지정하여
    - page.html에서 상단에 {% extends "base.html" %} 쓰고 {% block @@@ %}....{% endblock %} 으로 해당 블록을 불러서 재정의및 처리가 가능하다.

- Meta정보
    - 

- font awesome
    - 위 텍스트를 구글로 검색
    - 가입
    - 코드연결(CDN)
    - 폰트연결

- 2023-12-26
    - category : 일대다
    - blog_detail, base .html
    - admin
    - blog
        - model
        - urls
        - view
    
- 2023-12-27
    - hashtag(해시태그) : 다 대 다
    - models.py - Tag class 추가, Post class 에 tags생성
    - admin - Tag관련 생성
    - urls - Tag관련 생성
    - views - Tag관련 생성
    - post_list - Tag관련 생성
    - post_detail - Tag관련 생성
    - 

- 2023-12-28
    - settings.py - INSTALLED_APPS 에 'crispy_forms','marodownx', settings.py 맨 아래에 입력, CRISPY_TEMPLATE_PACK = 'bootstrap4' 추가
        - crispy_forms : 모양 form을 만드는 외부 라이브러리
        - marodownx : form자체를 사용하게 하는 것
        - CRISPY_TEMPLATE_PACK = 'bootstrap4' : bootstrap4를 사용하게
    - models.py
        - from markdownx.models import MarkdownField, from markdownx.utils import markdown 추가
        - content 수정
    
    - urls.py
        - import
            - redirect
            - from django.views.generic import ListView, DetailView, CreateView, UpdateView
            - from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
            - from django.utils.text import slugify   # 문자열을 url에 적합한 형태로 변환
            - from django.shortcuts import get_object_or_404  # 검색 조건이 안 맞으면 404에러를 반환
            - from django.core.exceptions import PermissionDenied
            - from django.db.models import Q # 데이터 베이스에서 데이터를 검색하거나 필터링 할 때, 다양한 조건을 조합하고 동적으로 쿼리를 작성하는 상황에서 사용
            - 

- 2024-01-03
    - serch기능 구현
    - urls.py search관련 추가
    - views.py search관련 추가
        - Q : Query객체 - 여러 개의 조건을 조합하고, OR 연산자로 묶어 쿼리를 작성할 수 있습니다. 일반적으로 Q 객체는 filter() 메서드의 매개 변수로 사용되어 데이터베이스에서 특정 조건을 만족하는 레코드를 검색하는 데 사용됩니다.
    - is_pagination : generic 에서 자동으로 생성된다.



    


## 로그인

#### 라이브러리 설치 : pip install django-allauth
#### INSTALLED_APPS 추가
- "django.contrib.sites", # 사이트 관리
- "allauth", # allauth 앱
- "allauth.account", # 계정 관리
- "allauth.socialaccount", # 소셜 계정 관리
- "allauth.socialaccount.providers.google", # 구글 로그인

#### AUTHENTICATION_BACKENDS 설정
AUTHENTICATION_BACKENDS = [ 
"django.contrib.auth.backends.ModelBackend",
"allauth.account.auth_backends.AuthenticationBackend", 
]
SITE_ID = 1 # 사이트 아이디

- ACCOUNT_EMAIL_REQUIRED = True # 회원가입시 이메일 필수 
- ACCOUNT_EMAIL_VERIFICATION = "none" # 이메일 인증 필요없음 
- LOGIN_REDIRECT_URL = "/blog/" # 로그인 후 이동 페이지

#### 구글 개발자 콘솔
- 새 프로젝트와 클라이언트 만들기 - console.developers.google.com 에 접속
- 새 프로젝트 생성 > 만들기 > OAuth 동의화면 외부 선택 > 앱이름
- 사용자 인증 정보 > 사용자 인증 정보 만들기 > OAuth 클라이언트 ID > 만들기 (유형, 이름, URL, URI 입력)
- 승인된 자바스크립트 원본 : http://127.0.0.1:8000
- 승인된 리디렉션 URI : http://127.0.0.1:8000/accounts/google/login/callback/

#### navbar {% load socialaccount %}

2024-01-04
    - settings.py - installed_apps [
    'django.contrib.sites',                     # 사이트 관리
    'allauth',                                  # allauth앱
    'allauth.account',                          # 게정 관리
    'allauth.socialaccount',                    # 소셜 계정 관리
    'allauth.socialaccount.providers.google',   # 구글 로그인
    ] - 추가
    - settings.py 아래에 
        AUTHENTICATION_BACKENDS = [
            # 사용자명과 비밀번호를 이용한 인증을 지원
            'django.contrib.auth.backends.ModelBackend',

            # 이메일 주소를 이용한 인증 등 추가적인 인증 방식을 지원
            'allauth.account.auth_backends.AuthenticationBackend',
        ]
        SITE_ID = 1 # 사이트 아이디 지정
        ACCOUNT_EMAIL_REQUIRED = True # 회원가입시 이메일 필수
        ACCOUNT_EMAIL_VERIFICATION = 'none' # 이메일 인증 필요 없음
        LOGIN_REDIRECT_URL = '/blog/' # 로그인 후 이동 페이지
        추가
    - mysite.urls.py - path('accounts/', include('allauth.urls')), 추가
    - navbar.html에서 {% if user.is_authenticated %} 부분 생성
    - navbar.html 에서 modal도 추가
    - console.developers.google.com - 접속 - 새 프로젝트 생성 > 만들기 
    -> 프로젝트 이름 : kitatest -> OAuth 동의화면 외부 선택 > 앱이름, 사용자 이메일 > 저장후 계속 >
    -> 사용자 인증 정보 -> 사용자 인증 정보 만들기 > Oauth 클라이언트ID만들기 > 어플리케이션 유형 > 웹 어플리케이션
    > 이름 : kitatest , 승인된 자바스크립트 원본 : http://127.0.0.1:8000, 승인된 리디렉션 URI : http://127.0.0.1:8000/accounts/google/login/callback/ > 만들기 > 아이디,비밀번호 저장 & json 다운로드
        - 클라이언트 아이디 : 657243800148-vpcspg262qc34tljoru213e0e7qffo1k.apps.googleusercontent.com
        - 클라이언트 비밀번호: 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
    -> python manage.py makemigrations, python manage.py migrate > python manage.py runserver > admin 접속
    -> admin페이지에서 site > example.com 을 수정 >Domain name : 127.0.0.1:8000, Display name: local development
> save 
    -> social application > add > Provider: Google 선택 name : google, Client id: 클라이언트 아이디, Secret key: 클라이언트 비밀번호, Sites: 127.0.0.1:8000 -> 로 이동 > save
    -> navbar.html 맨위에 {% load socialaccount %} 작성
    
- 2024-01-05
    - Recent post기능 개발
        - single_pages/landing.html 작업
        - single_pages/views.py 작업
    - news기능 개발
        - python manage.py startapp data > data앱 생성
        - settings.py > 'data', 추가
        - data > urls.py 생성
        - mysite.urls.py > path('data/', include('data.urls')), 추가
        - data > urls.py > path('', views.news_search, name='news_search'), 추가
        - data > views.py > def news_search(request): 함수생성 
            - import requests 추가
            - from bs4 import BeautifulSoup 추가
        - 