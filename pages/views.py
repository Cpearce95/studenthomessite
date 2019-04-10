from django.shortcuts import render
from django.http import HttpResponse
from listings.choices import price_choices, bedroom_choices, nearestuni_choices

from listings.models import Listing
from advisors.models import Advisor


def index(request):
    listings = Listing.objects.order_by('-list_date').filter (is_published=True)[:3]

    context = {
        'listings': listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'nearestuni_choices': nearestuni_choices
    }

    return render(request, 'pages/index.html', context)

def about(request):
    #Get all advisors
    advisors = Advisor.objects.order_by('-hire_date')

    # Get MVP
    mvp_advisors = Advisor.objects.all().filter(is_mvp=True)

    context = {
        'advisors': advisors,
        'mvp_advisors': mvp_advisors
    }

    return render(request, 'pages/about.html', context)
