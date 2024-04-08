from django.urls import path,include
from .import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.startPage),
    path('account/',include("django.contrib.auth.urls")),
    path('login/',views.loginPage, name='login'),
    path('signup/',views.signupPage,name='signup'),
    path('success/',views.success_view,name='success'),
    path('complaint/',views.complaintPage,name='complaint'),
    path('submitedSuccessfully/',views.complaintPostedPage, name='complaintPosted')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
