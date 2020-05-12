from data import data_manager
import psycopg2
import psycopg2.extras
from psycopg2 import sql



def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_given_show(show_id):
    return data_manager.execute_select(f'SELECT * FROM shows WHERE id = %(id)s;', {"id": show_id})[0]


def get_seasons_list(show_id=None):
    return data_manager.execute_select(f'SELECT * FROM seasons WHERE show_id = %(id)s;', {"id": show_id})


def get_given_season(season_id):
    return data_manager.execute_select(f'SELECT * FROM seasons WHERE id = %(id)s;', {'id': season_id})


def get_genres_list(show_id):
    return data_manager.execute_select(
        f'SELECT name FROM genres right join show_genres on genres.id = show_genres.genre_id WHERE show_id = %(id)s;',
        {"id": show_id})


def get_given_episode(episode_id):
    return data_manager.execute_select(
        f'SELECT * FROM episodes WHERE id = %(id)s;',
        {"id": episode_id})


def query_artists_by_movies_count(min_movies):
    # print(data_manager.execute_select(f'SELECT name, count(show_id) as "number_of_movies" FROM actors join show_characters on actors.id = show_characters.actor_id group by name having count(show_id) > %(min_movies)s order by number_of_movies desc;', {'min_movies':min_movies}))
    return data_manager.execute_select(
        f'SELECT name, count(show_id) as "number_of_movies" FROM actors join show_characters on actors.id = show_characters.actor_id group by name having count(show_id) >= %(min_movies)s order by number_of_movies desc;',
        {'min_movies': min_movies})


def add_actor(actor_date):
    insert_query = f"INSERT INTO actors ( name, birthday, death, biography) VALUES ( %(name)s, %(birthday)s, %(death)s , %(biography)s);"
    data_manager.execute_insert(insert_query, actor_date)


def get_all_genres():
    return data_manager.execute_select(f'SELECT name FROM genres;')


def get_show_by_genres(genres_id):
    return data_manager.execute_select(f'SELECT title, year, rating FROM shows WHERE shows.')


def get_n_sorted_actors(range, page, sort_by, order):
    # query = f"""select name, birthday, death, biography
    #         from actors
    #         order by {sort_by} {order}
    #         limit %s offset ( (%s - 1) * %s);"""

    query2 = sql.SQL(f""" select name, birthday, death, biography 
                from actors
                order by {sort_by} {order}  
                limit %s offset ( (%s - 1) * %s);
                """).format(sort_by=sql.Identifier(sort_by), order=sql.Identifier(order))

    return data_manager.execute_select(query2, (range, page, range,))

