from django.http import HttpResponse
from django.views import View

# from .forms  import GuitarForm
from .models import Guitar


class GuitarListView(View):
    """ listview """
    def get(self, request):

        return HttpResponse("Hello World!")


class GuitarDetailView(View):
    """ detailview """


class GuitarUpdateView(View):
    """ updateview """


class GuitarCreateView(View):
    """ createview """


class GuitarDeleteView(View):
    """ deleteview """
