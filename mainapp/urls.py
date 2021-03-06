"""mainapp URL Configuration

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
from BugTrackingTool.views import ( BugApiView, BugDetailsApiView,
                                   MemberApiView, MemberDetailsApiView,
                                   ProjectApiView, ProjectDetailsApiView,
                                   BugStatusChangeAPIView, StatusApiView, 
                                   StatusDetailsApiView,BugSolvedAPIView )
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('member', MemberApiView.as_view(), name='member'),
    path('memberDetails/<pk>/', MemberDetailsApiView.as_view(),name='memberDetails'),
    path('project', ProjectApiView.as_view(), name='project'),
    path('projectDetails/<pk>/', ProjectDetailsApiView.as_view(),name='projectDetails'),
    path('bug', BugApiView.as_view(), name='bug'),
    path('bugDetails/<pk>/',BugDetailsApiView.as_view(),name='bugDetails'),
    path('status', StatusApiView.as_view(), name='status'),
    path('statusDetails/<pk>/', StatusDetailsApiView.as_view(),name='statusDetails'),
    path('bugStatusChange/<pk>/', BugStatusChangeAPIView.as_view(), name='bugStatusChange'),
    path('bugSolvedList', BugSolvedAPIView.as_view(), name='bugSolvedList'),
]
