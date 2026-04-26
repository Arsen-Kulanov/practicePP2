import psycopg2
from config import *

conn = psycopg2.connect(
    host=host,
    user=user,
    password=password,
    dbname=db_name,
    port=port
)


def get_player_id(username):
    cur = conn.cursor()

    try:
        cur.execute("SELECT id FROM players WHERE username=%s", (username,))
        result = cur.fetchone()

        if result:
            return result[0]

        cur.execute(
            "INSERT INTO players (username) VALUES (%s) RETURNING id",
            (username,)
        )
        player_id = cur.fetchone()[0]

        conn.commit()
        return player_id

    except Exception as e:
        conn.rollback()
        print("DB error:", e)
        return None

    finally:
        cur.close()


def save_game(username, score, level):
    player_id = get_player_id(username)

    if player_id is None:
        return

    cur = conn.cursor()

    try:
        cur.execute("""
            INSERT INTO game_sessions (player_id, score, level_reached)
            VALUES (%s, %s, %s)
        """, (player_id, score, level))

        conn.commit()

    except Exception as e:
        conn.rollback()
        print("DB error:", e)

    finally:
        cur.close()


def get_top10():
    cur = conn.cursor()

    try:
        cur.execute("""
            SELECT p.username, g.score, g.level_reached, g.played_at
            FROM game_sessions g
            JOIN players p ON p.id = g.player_id
            ORDER BY g.score DESC
            LIMIT 10
        """)

        data = cur.fetchall()
        return data

    except Exception as e:
        print("DB error:", e)
        return []

    finally:
        cur.close()