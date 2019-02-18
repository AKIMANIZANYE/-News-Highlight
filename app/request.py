from app import app
import urllib.request,json
from .Models import News

News=News.News

# api_key = app.config['News_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]

api_key = app.config['NEWS_API_KEY']
def get_new(category):
    '''
    Function that gets the json response to our url request
    '''
    get_news_url = base_url.format(category,api_key)

    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        news_results = None

        if get_news_response['results']:
           news_results_list = get_news_response['results']
           news_results = process_results(news_results_list)
def process_results(news_list):
    
    news_results = []
    for news_item in news_list:
            
        id = news_item.get('id')
        title = news_item.get('original_title')
        name =news_item.get('name')
        author=news_item.get('author')
        description=news_item.get('description')
        url=news_item.get('link')
        urlToImage=news_item.get('image')
        publishedAt=news_item.get('date')
        poster = news_item.get('poster_path')
        

        if poster:
            news_object = News(id,title,overview,poster,vote_average,vote_count)
            news_results.append(news_object)

    return news_results

def get_news(id):
    get_new_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_new_details_url) as url:
        new_details_data = url.read()
        new_details_response = json.loads(new_details_data)

        new_object = None
        if new_details_response:
                id = news_details_response.get('id')
                title = news_details_response.get('title')
                name = news_details_response.get('name')
                author=news_details_response.get('author')
                description=news_details_response.get('description')
                url=news_details_response.get('link')
                urlToImage=news_details_response.get('image')
                publishedAt=news_details_response.get('date')
                poster = news_details_response.get('poster_path')
                new_object = News(id,title,name,author,description,url,urlToImage,publishedAt,poster)

    return new_object
def search_new(new_name):
    search_new_url = 'https://newsapi.org/v2/everything?q=bitcoin&from=2019-01-18&sortBy=publishedAt&apiKey=870c6f91cc3244ac9013dcbecb84e54d?api_key={}&query={}'.format(api_key,new_name)
    with urllib.request.urlopen(search_movie_url) as url:
        search_new_data = url.read()
        search_new_response = json.loads(search_new_data)

        search_new_results = None

        if search_new_response['results']:
            search_new_list = search_new_response['results']
            search_new_results = process_results(search_new_list)


    return search_new_results 