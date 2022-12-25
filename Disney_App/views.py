from django.shortcuts import render
from .models import Movies
from django.db import connection
from datetime import datetime


def dictfetchall(cursor):
    # Return all rows from a cursor as a dict
    columns = [col[0] for col in cursor.description]
    return [dict(zip(columns, row)) for row in cursor.fetchall()]


def home():
    return None


def index(request):
    with connection.cursor() as cursor:
        cursor.execute("""
                        SELECT movieTitle,genre
                        FROM Movies
                        WHERE genre='Comedy'
                        """)
        sql_res = dictfetchall(cursor)
    return render(request, 'index.html', {'sql_res': sql_res})


def add_a_movie(request):
    if request.method == 'POST' and request.POST:
        new_title = request.POST["title"]
        new_date = request.POST["release_date"]
        new_genre = request.POST["genre"]
        new_rating = request.POST["rating"]
        new_gross = request.POST["gross"]
        new_content = Movies(movieTitle=new_title,
                             releasedate=new_date,
                             genre=new_genre,
                             rating=new_rating,
                             gross=new_gross
                             )
        new_content.save()
    return render(request, 'add_a_movie.html')


def query_results(request):
    if request.method == 'POST' and request.POST:
        new_title = request.POST["title"]
        new_language = request.POST["language"]
        # today = datetime.today().strftime('%Y-%m-%d')
        new_content = Movies(movieTitle=new_title,
                             genre=new_language)
        new_content.save()
    return render(request, 'add_a_movie.html')
