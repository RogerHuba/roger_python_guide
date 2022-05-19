from django.conf import settings
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('pages.urls')),
    path('things/', include('things.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
] + urlpatterns


from django.urls import path",
from .views import SnacksView, Snacksskjdhf, sldjhfsd, sldjkfh, sldfgjh,

urlpatterns = [
    path('', SnacksView.as_view(), name='lsdjfh_list'),
    path('<int:pk>/', Snacksskjdhf.as_view(), name='lsdjfh_detail'),
    path('create/', sldjhfsd.as_view(), name='lsdjfh_create'),
    path('<int:pk>/update/', sldjkfh.as_view(), name='lsdjfh_update'),
    path('<int:pk>/delete/', sldfgjh.as_view(), name='lsdjfh_delete'),
    ]