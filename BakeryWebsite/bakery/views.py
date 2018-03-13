from django.shortcuts import render
import urllib.request
import urllib.parse
import json

# Create your views here.
def bakeryItemDetails(request, pk):

    req = urllib.request.Request('http://exp-api:8000/bakeryItem/' + str(pk) + '/')

    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    context = {
        'bakeryItem': resp,
    }
    return render(request, 'bakery/bakeryItem_detail.html', context)


def index(request):

    req = urllib.request.Request('http://exp-api:8000/bakeryItem/(?P<pk>\d+)')

    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)
    context = {
        'bakeryItem_list': resp,
    }
    return render(request, 'bakery/index.html', context)


#class bakeryItemListView(generic.ListView):
 #   model = bakeryItem

#class bakeryItemDetailView(generic.DetailView):
 #   model = bakeryItem
