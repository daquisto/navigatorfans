from django.views import generic

from .forms  import GuitarForm
from .models import Guitar


class GuitarListView(generic.ListView):
    model = Guitar


class GuitarDetailView(generic.DetailView):
    model = Guitar


class GuitarEditView(generic.edit.FormView):
    template_name = 'guitars/guitar_edit.html'
    form_class = GuitarForm





