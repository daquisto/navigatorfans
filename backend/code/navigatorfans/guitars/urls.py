from django.urls import path


from .views import GuitarDetailView, GuitarListView, GuitarEditView

urlpatterns = [
    path('', GuitarListView.as_view(), name='guitarview'),
    path('guitar/<int:pk>', GuitarDetailView.as_view(), name='guitaredit'),
    path('guitar_edit/<int:pk>', GuitarEditView.as_view(), name='guitaredit'),
]