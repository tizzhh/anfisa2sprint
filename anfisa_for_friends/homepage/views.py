from django.shortcuts import render
from django.db.models import Q
from ice_cream.models import IceCream


def index(request):
    template = 'homepage/index.html'
    ice_cream_list = IceCream.objects.values('title', 'id', 'description').filter(is_on_main=True, is_published=True).order_by('title')[1:4]
    # ice_cream_list = IceCream.objects.values('title', 'id', 'description').filter(
    #     Q(is_published=True) & (Q(is_on_main=True) | Q(title__contains='пломбир'))
    # )
    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)