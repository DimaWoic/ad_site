from django.shortcuts import render
from .models import AdBoard

# Create your views here.


def index(request):
    adds = AdBoard.objects.all()
    context = {'adds': adds}
    return render(request, template_name='board/index_adds.html', context=context)


