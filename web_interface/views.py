from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView
# from scrapyd_api import ScrapydAPI

from web_interface.models import ScrapyItem

# scrapyd = ScrapydAPI('http://localhost:6800')


class QuotesListView(View):
    # model = ScrapyItem
    # # fields = ['title', 'author']
    # template_name = 'web_interface/quotesList.html'


    def get(self,request):
        quotes = ScrapyItem.objects.all()
        # fields = ['title', 'author']
        return render(request,'web_interface/quotesList.html',{'quotes_list':quotes})
    # template_name = 'web_interface/quotesList.html'