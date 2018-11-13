from flask import render_template
from app import app

#Views
@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    #Getting popular news highlights
    # popular_news  = get_news('popular')

    title = 'Home - Welcome to The best News Highlights Website Online'
    return render_template('index.html', title = title)


@app.route('/news/<int:news_id>')
def news(news_id):

    '''
    View news page function that returns the news details page and its data
    '''
    return render_template('news.html',id = news_id)