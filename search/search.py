import requests
from .translate import translate_rt

def search(query):
    url_search = 'https://searx.roughs.ru/search?q={}&engines=google&format=json&safesearch=1'
    res = requests.get(url_search.format(query)).json()
    n_result = int(res['number_of_results'])
    k = res["results"][-1]["positions"][0]
    results = []
    for i in range(k):
        result = {
         'title': res["results"][i]["title"],
         'parsed_url': res["results"][i]["parsed_url"][1],
         'url': res["results"][i]["url"],
         'content': res["results"][i]["content"],
        }
        results.append(result)

    return results, n_result

def search_t(query):
    url_search = 'https://searx.roughs.ru/search?q={}&engines=google&format=json&safesearch=1'
    res = requests.get(url_search.format(query)).json()
    n_result = int(res['number_of_results'])
    k = res["results"][-1]["positions"][0]
    results = []
    for i in range(k):
        result = {
         'title': translate_rt(res["results"][i]["title"]),
         'parsed_url': res["results"][i]["parsed_url"][1],
         'url': res["results"][i]["url"],
         'content': translate_rt(res["results"][i]["content"]),
        }
        results.append(result)

    return results, n_result
