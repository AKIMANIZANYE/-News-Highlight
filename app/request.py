
import urllib.request,json
from .Models import News
from app import app

News=News.News
source = news.source

api_key = app.config['NEWS_API_KEY']
source_base_url= app.config["NEWS_SOURCES_BASE_URL"]
News_base_url = app.config["NEWS_API_BASE_URL"]
def get_sources(category):
        '''
        Function that gets the json response to our url request
        '''
        get_sources_url =source_base_url.format(category,api_key)
        print(get_news_url)

        with urllib.request.urlopen(get_sources_url) as url:
                get_sources_data = url.read()
                get_sources_response = json.loads(get_sources_data)
                news_articles = None

                if get_sources_response['sources']:
                        sources_articles_list = get_sources_response['sources']
                        sources_articles = process_articles(sources_articles_list)
        
        return sources_articles

def process_articles(sources_list):
    
       source_articles= []
       for news_item in news_list:
                
                id = news_item.get('id')
                title = news_item.get('title')
                name =news_item.get('name')
                author=news_item.get('author')
                description=news_item.get('description')
                url=news_item.get('url')
                urlToImage=news_item.get('urlToImage')
                publishedAt=news_item.get('publishedAt')
                content=news_item.get('content')

                if urlToImage:
                       news_object = Source(id,title,name,author,description,url, urlToImage,publishedAt)
                       news_articles.append(news_object)

        return news_articles

def get_new(id):
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
                        url=news_details_response.get('url')
                        urlToImage=news_details_response.get(' urlToImage')
                        publishedAt =news_details_response.get('publishedAt')
                        content = news_details_response.get('content')
                        new_object = News(id,title,name,author,description,url,urlToImage,publishedAt,poster)

        return new_object
def search_new(new_name):
        search_new_url = 'https://newsapi.org/v2/everything?q=bitcoin&from=2019-01-18&sortBy=publishedAt&apiKey=870c6f91cc3244ac9013dcbecb84e54d?api_key={}&query={}'.format(api_key,new_id)
        with urllib.request.urlopen(search_new_url) as url:
                search_new_data = url.read()
                search_new_response = json.loads(search_new_data)
                search_new_articles = None

                if search_new_response['articles']:
                        search_new_list = search_new_response['articles']
                        search_new_articles = process_articles(search_new_list)


        return search_new_articles