from django.shortcuts import render
import requests
from .models import Query
from .forms import SearchForm
from .search import search, search_t
from .translate import translate_tr

def index(request):
    if request.method == "POST":
        query = SearchForm(request.POST)
        query = str(query)[56:-50]
        search_query, n_result = search(query)
        query_t = translate_tr(query)
        search_t_query_t, n_result_t = search_t(query_t)
        context = {**{'all_info': search_query}, **{'all_info_t': search_t_query_t}}
        increase = round((n_result_t-n_result)/n_result*100)
        query_db = Query(query = query, n_result = n_result, query_t = query_t, n_result_t = n_result_t, increase = increase)
        query_db.save()
        return render(request, 'search/index.html', context)

    return render(request, 'search/index.html')

def statistic(request):
    querys = Query.objects.all()
    return render(request, 'search/statistic.html', {'querys': querys})
