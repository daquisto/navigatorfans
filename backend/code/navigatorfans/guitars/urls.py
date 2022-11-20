from django.urls import path


from .views import GuitarListView

urlpatterns = [
    path('', GuitarListView.as_view(), name='guitarview')
]