class Config:
    '''
    General configuration parent class
    '''
    NEWS_API_BASE_URL ='https://newsapi.org/v2/everything?q=bitcoin&sortBy=publishedAt&apiKey={}'
    NEWS_SOURCES_BASE_URL='https://newapi.org/v2/sources?category&apiKey=870c6f91cc3244ac9013dcbecb84e54d'
    NEWS_API_KEY ='870c6f91cc3244ac9013dcbecb84e54d'
    pass



class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True