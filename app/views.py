from flask import render_template
from app import app
from .request import get_news,get_new
@app.route('/')
def index():
        '''
        View movie page function that returns the movie details page and its data
        '''
        new= get_news(id)
        title = f'{new.title}'  

        popular_news = get_news('popular')
        print(popular_news)
        message = 'welcome to New Highlight'
        return render_template('index.html')
        return render_template('news.html',id =news_id)
        title = 'Home - Welcome to The best news  Review Website Online'
        return render_template('index.html', title = title,popular = popular_news,upcoming = upcoming_news, now_showing = now_showing_news,new = new)
# @app.route('/news/<int:id>')
# def news(id):
