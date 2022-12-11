from django.urls import path


from .views import GuitarCreateView, GuitarDeleteView, GuitarDetailView, GuitarListView, GuitarUpdateView

urlpatterns = [
    path('', GuitarListView.as_view(), name='guitarview'),
    path('guitar/<int:pk>', GuitarDetailView.as_view(), name='guitardetail'),
    path('guitar/<int:pk>/edit', GuitarUpdateView.as_view(), name='guitaredit'),
    path('guitar/create', GuitarCreateView.as_view(), name='guitarcreate'),
    path('guitar/<int:pk>/delete', GuitarDeleteView.as_view(), name='guitardelete'),
]