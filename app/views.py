from flask import render_template,request,redirect,url_for
from app import app
from .request import get_news,get_new,search_new
from .Models import reviews
from .forms import ReviewForm
Review = reviews.Review
@app.route('/')
def index():
        '''
        View movie page function that returns the movie details page and its data
        '''
        new=get_new(id)
               
        popular_news = get_news('popular')
        upcoming_news=get_news('upcoming')
        now_showing_news=get_news('now playing')
        title = 'Home - Welcome to The best news  Review Website Online'
        # search_new=request.args.get('new_query')
        # if search_new:
        #         return redirect(url_for('search',new_name=search_new))
        # else:
        return render_template('index.html', title = title,popular = popular_news,upcoming = upcoming_news, now_showing = now_showing_news)
                # @app.route('/news/<int:id>')
                # def news(id):

@app.route('/search/<new_name>')
def search(new_name):
        new_name_list = new_name.split(" ")
        new_name_format = "+".join(new_name_list)
        searched_news = search_new(new_name_format)
        title = f'search articles" for {new_name}'
        return render_template('search.html',news = searched_news)

@app.route('/new/review/new/<int:id>', methods = ['GET','POST'])
def new_review(id):
        form = ReviewForm()
        new= get_new(id)

        if form.validate_on_submit():
                title = form.title.data
                name = form.name.data
                new_name = Review(new.id,title,name,author,description,urlToImage,url,publishedAt,content)
                new_review.save_review()
                return redirect(url_for('new',id = movie.id ))

        title = f'{new.title} review'
        return render_template('new_review.html',title = title, review_form=form, new=new)