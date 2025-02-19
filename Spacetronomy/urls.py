from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('contact', views.contact, name="Contact"),
    path('about', views.about, name="About"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
