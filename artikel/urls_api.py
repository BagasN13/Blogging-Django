from django.urls import path, include
from django.contrib import admin
from artikel.api import (
    api_Blogpost_list,
    api_Blogpost_tambah,
    api_Blogpost_update,
    api_Blogpost_delete,
)

urlpatterns = [
    #################### API GOOGLE AUTH ###########################################
    path('accounts/', include("allauth.urls")),


    ######################## API ARTIKEL ##########################################################################################################
    path('artikel/list', api_Blogpost_list),
    path('artikel/tambah', api_Blogpost_tambah),
    path('artikel/update<int:id_artikel>', api_Blogpost_update),
    path('artikel/delete<int:id_artikel>', api_Blogpost_delete),

]
