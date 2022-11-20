from django.views import generic

from .models import Guitar


class GuitarListView(generic.ListView):
    model = Guitar




