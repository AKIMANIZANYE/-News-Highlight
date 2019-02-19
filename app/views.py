from flask import render_template,request,redirect,url_for
from app import app
from .request import get_news,get_new,search_new
from .models import review
from .forms import ReviewForm
Review = review.Review
@app.route('/')
def index():
        '''
        View movie page function that returns the movie details page and its data
        '''
        new= get_news(id)
        title = f'{new.title}'  

        popular_news = get_news('popular')
        upcoming_news=get_news('upcoming')
        now_showing=get_news('now playing')
       title = 'Home - Welcome to The best news  Review Website Online'
       search_new=request.args.get('new_query')
       if search_new:
        return render_redirect(url_for('seach',new_name=search_new)
       else:
        
        return render_template('index.html', title = title,popular = popular_news,upcoming = upcoming_news, now_showing = now_showing_news,new = new)
# @app.route('/news/<int:id>')
# def news(id):

@app.route('/search/<new_name>')
def search(new_name):
        new_name_list = new_name.split(" ")
        new_name_format = "+".join(new_name_list)
        searched_news = search_new(new_name_format)
        title = f'search results for {new_name}'
        return render_template('search.html',news = searched_news