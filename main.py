from flask import Flask, render_template, url_for, request, redirect
from data import queries
from util import json_response
import sys

app = Flask('codecool_series')


@app.route('/')
def index():
    genres = queries.get_all_genres()
    shows = queries.get_shows()
    return render_template('index.html', shows=shows, genres=genres)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/tv-show/<tv_show_id>')
def show_given_series(tv_show_id=None):
    show_details = queries.get_given_show(tv_show_id)
    seasons_details = queries.get_seasons_list(tv_show_id)
    print(seasons_details)
    genres = ''
    for genre in queries.get_genres_list(tv_show_id):
        genres += genre['name'] + ', '

    genres = genres.rstrip(', ')
    tv_show_name = show_details['title']

    return render_template("tv_show_details.html", show_details=show_details, seasons_details=seasons_details,
                           genres=genres, tv_show_id=tv_show_id, tv_show_name=tv_show_name)


@app.route('/tv-show/modal/<tv_show_id>')
@json_response
def get_seasons_list(tv_show_id=None):
    try:
        tv_show_id = int(tv_show_id)
        print(queries.get_seasons_list(tv_show_id))
        return queries.get_seasons_list(tv_show_id)
    except ValueError as err:
        print(f"our error: Only strings")
        return f"our error: {sys.exc_info()[0]}"
    except:
        print("Unexpected error:", sys.exc_info()[0])


@app.route('/artists/min-movies', methods=['get'])
def get_artists_by_movies_count():
    min_movies = request.args.get("min")
    # print(request.args.get("min"))
    artists_by_movies_count = queries.query_artists_by_movies_count(min_movies)
    return render_template('artist.html', artists_list=artists_by_movies_count)


@app.route('/tv-show/<tv_show_id>/<season_id>', methods=["get"])
def get_season(tv_show_id=None, season_id=None):
    single_season_details = queries.get_given_season(season_id)[0]
    tv_show_name = str(request.args.get('tv_show_name'))
    season = single_season_details['season_number']
    print(tv_show_name)
    return render_template("tv_show_season.html", season=season, single_season_details=single_season_details,
                           tv_show_name=tv_show_name, tv_show_id=tv_show_id)


@app.route('/tv-show/<tv_show_id>/<season_id>/<episode_id>', methods=["get"])
def get_episode(tv_show_id=None, season_id=None, episode_id=None):
    episode_details = queries.get_given_episode(episode_id)
    tv_show_name = request.args.get['tv_show_name']
    season = request.args.get['season']
    return render_template("tv_show_episode.html", season=season,
                           tv_show_name=tv_show_name, tv_show_id=tv_show_id, season_id=season_id,
                           episode_details=episode_details)


@app.route('/add-actor', methods=["POST", "GET"])
def add_actor():
    if request.method == "GET":
        return render_template('add_actor.html')
    elif request.method == "POST":
        actor_data = dict(request.form)
        if actor_data["death"] == "":
            actor_data["death"] = None
            print(actor_data)
        queries.add_actor(actor_data)
        return redirect('/')


@app.route('/<genre>')
def get_shows_by_genre(genre=None):
    shows_by_genre = queries.get_show_by_genres(genre)
    return render_template('artist.html')


@app.route('/actors-list/<actor_range>/<page>/<sort_by>/<order>', methods=["POST", "GET"])
@app.route('/actors-list/',  methods=["POST", "GET"])
def show_list_with_n_actors(actor_range=None, page=1, sort_by="name", order="ASC"):
    print('im here')
    # if not actor_range:
    print('if wszedl')
    actor_range = request.args.get('range')
    print(actor_range)
    results = queries.get_n_sorted_actors(actor_range, page, sort_by, order)

    print(results)
    return render_template('actors_list.html', results=results, actor_range=actor_range, page=page, sort_by=sort_by, order=order)


def main():
    app.run(
        debug=True,
        # host='0.0.0.0',
        port=7001
    )


if __name__ == '__main__':
    main()
