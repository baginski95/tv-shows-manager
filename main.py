from flask import Flask, render_template, url_for
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
    genres = queries.get_genres_list(series_id)
    print(show_details)
    print(seasons_details)
    print(queries.get_genres_list(series_id))

    return render_template("tv_show_details.html", show_details=show_details, seasons_details=seasons_details, genres=genres, tv_show_id=tv_show_id)

def main():
    app.run(
        debug=True,
        # host='0.0.0.0',
        port=7001
    )


if __name__ == '__main__':
    main()
