from flask import Flask, render_template, url_for, request
from data import queries

app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/tv-show/<tv_show_id>')
def show_given_series(tv_show_id=None):
    series_id = int(tv_show_id)
    show_details = queries.get_given_show(series_id)
    seasons_details = queries.get_seasons_list(series_id)
    genres = ''
    for genre in queries.get_genres_list(series_id):
        genres += genre['name'] + ', '

    genres = genres.rstrip(', ')
    tv_show_name = show_details['title']

    return render_template("tv_show_details.html", show_details=show_details, seasons_details=seasons_details,
                           genres=genres, tv_show_id=tv_show_id, tv_show_name=tv_show_name)


@app.route('/tv-show/<tv_show_id>/<season_id>', methods=["get"])
def get_season(tv_show_id=None, season_id=None):
    single_season_details = queries.get_given_season(season_id)
    tv_show_name = request.args.get()
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


def main():
    app.run(
        debug=True,
        # host='0.0.0.0',
        port=7001
    )


if __name__ == '__main__':
    main()
