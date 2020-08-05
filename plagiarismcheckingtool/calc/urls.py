from django .urls import path
from . import views
from .import myviews
urlpatterns=[
path("",views.home,name='home'),
path("check",views.check,name='check'),
path("rename",views.rename,name='rename'),
path("fileHandle",views.fileHandle,name='fileHandle'),
path("text",views.text,name="text")
]
