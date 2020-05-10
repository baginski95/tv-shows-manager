from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_given_show(show_id):
    return data_manager.execute_select(f'SELECT * FROM shows WHERE id = %(id)s;', {"id": show_id})[0]


def get_seasons_list(show_id):
    return data_manager.execute_select(f'SELECT * FROM seasons WHERE show_id = %(id)s;', {"id": show_id})


def get_given_season(season_id):
    return data_manager.execute_select((f'SELECT * FROM seasons WHERE id = %(id)s;', {'id': season_id}))


def get_genres_list(show_id):
    return data_manager.execute_select(
        f'SELECT name FROM genres right join show_genres on genres.id = show_genres.genre_id WHERE show_id = %(id)s;',
        {"id": show_id})


def get_given_episode(episode_id):
    return data_manager.execute_select(
        f'SELECT * FROM episodes WHERE id = %(id)s;',
        {"id": episode_id})
