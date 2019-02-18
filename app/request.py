from app import app
import urllib.request,json
from .Models import News

News=News.News

# api_key = app.config['News_API_KEY']

# Getting the movie base url
base_url = app.config["NEWS_API_BASE_URL"]

api_key = app.config['NEWS_API_KEY']
def get_news(category):
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
    get_news_details_url = base_url.format(id,api_key)

    with urllib.request.urlopen(get_movie_details_url) as url:
        news_details_data = url.read()
        news_details_response = json.loads(movie_details_data)

        news_object = None
        if news_details_response:
            id = news_details_response.get('id')
            title = news_details_response.get('original_title')
            name = news_details_response.get('overview')
            author=news_details_response.get('author')
            description=news_details_response.get('description')
            url=news_details_response.get('link')
            urlToImage=news_details_response.get('image')
            publishedAt=news_details_response.get('date')
            poster = news_details_response.get('poster_path')
            

           news_object = News(id,title,name,author,description,url,urlToImage,publishedAt,poster)

    return news_object