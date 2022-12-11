from django.views import generic, View

# from .forms  import GuitarForm
from .models import Guitar


class BaseView(View):
    model = Guitar
    fields = '__all__'
    success_url = '/'


class GuitarListView(BaseView, generic.ListView):
    """ listview """


class GuitarDetailView(BaseView, generic.DetailView):
    """ detailview """


class GuitarUpdateView(BaseView, generic.UpdateView):
    """ updateview """


class GuitarCreateView(BaseView, generic.CreateView):
    """ createview """


class GuitarDeleteView(BaseView, generic.DeleteView):
    """ deleteview """
