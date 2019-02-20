from flask import render_template,request,redirect,url_for
from app import app
from .request import get_news,search_new, get_sources
from .Models import reviews
from .forms import ReviewForm
Review = reviews.Review
@app.route('/')
def index():
        '''
        View movie page function that returns the movie details page and its data
        '''
        # new=get_news(id)
               
        popular_news = get_sources('popular')
        # upcoming_news=get_sources('upcoming')
        # now_showing_news=get_sources('now playing')
        title = 'Home - Welcome to The best news  Review Website Online'
        # search_new=request.args.get('new_query')
        # if search_new:
        #         return redirect(url_for('search',new_name=search_new))
        # else:
        # print(popular_news)
        return render_template('index.html', title = title,popular = popular_news)
                # @app.route('/news/<int:id>')
                # def news(id):

@app.route('/search/<new_name>')
def search(new_name):
        new_name_list = new_name.split(" ")
        new_name_format = "+".join(new_name_list)
        searched_news = search_new(new_name_format)
        title = f'search articles" for {new_name}'
        return render_template('search.html',news = searched_news)

@app.route('/new/<id>')
def new_review(id):
        # form = ReviewForm()
        news= get_news(id)
        # print(new)

        # if form.validate_on_submit():
        #         title = form.title.data
        #         name = form.name.data
        #         new_name = Review(new.id,title,name,author,description,urlToImage,url,publishcontent)
        #         new_review.save_review()
        #         return redirect(url_for('new',id = movie.id ))

        title = 'Article'
        return render_template('news.html',title = title, news=news)