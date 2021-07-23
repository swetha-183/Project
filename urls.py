from django.urls import path
from FoodApp import views
from django.contrib.auth import views as v

urlpatterns =[
    path('',views.home,name="hm"),
    path('abt/',views.about,name="ab"),
    path('cnt/',views.contact,name="co"),
    path('lo/',v.LoginView.as_view(template_name="app_html/login.html"),name="log"),
     path('lou/',v.LogoutView.as_view(template_name="app_html/logout.html"),name="logo"),
    path('re/',views.register,name="reg"),
    path('it/',views.ilist,name="il"), # this url is for sweet
    path('swup/<int:m>/',views.swup,name="swup"),
    path('swdlt/<int:n>/',views.swdlt,name="swdl"),
    path('swv/<int:q>/',views.swviw,name="swvw"),
    path('sp/',views.swp,name="sp"),

    #Snacks:
    path('sn/',views.snalist,name="snac"),
    path('sup/<int:r>/',views.supt,name="supd"),
    path('sdlt/<int:s>/',views.sdl,name="sdlt"),
    path('snvw/<int:l>/',views.snvi,name="snvew"),
    path('snl/',views.snl,name="snli"),

    #MilkShake
    path('mi/',views.milk,name="milsh"),
    path('miup/<int:d>/',views.miu,name="miu"),
    path('mdl/<int:j>/',views.midl,name="mdlt"),
    path('milvw/<int:p>',views.milviw,name="milview"),
    path('mils/',views.milke,name="mik"),

    path('roletyp/',views.roletype,name='rlrq'),
    path('gvp/',views.gveperm,name="gvpe"),
    path('gvup/<int:t>/',views.gvu,name="gvupe"),
    # Buy Now
    path('add/',views.addt,name="addto"),
   

    
]