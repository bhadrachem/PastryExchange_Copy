from django.shortcuts import render
import urllib.request
import urllib.parse
import json

# Create your views here.
def index(request):
    return render(request, 'bakery/index.html')

def bakeryItemDetails(request, pk):
    print ("About to perform the GET request...")

    req = urllib.request.Request('http://exp-api:8000/bakeryItem/' + pk + '/')

    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)



def bakeryItemRecentList(request):
    print ("About to perform the GET request...")

    req = urllib.request.Request('http://exp-api:8000/bakeryItem/(?P<pk>\d+)')

    resp_json = urllib.request.urlopen(req).read().decode('utf-8')
    resp = json.loads(resp_json)

    print(resp)

#class bakeryItemListView(generic.ListView):
 #   model = bakeryItem

#class bakeryItemDetailView(generic.DetailView):
 #   model = bakeryItem
