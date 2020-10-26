import sqlite3
import json

from models import Mood

def get_all_moods():
    with sqlite3.connect('../../dailyjournal.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            m.id,
            m.label
        FROM moods m
        """)

        moods = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            mood = Mood(row['id'], row['label'])

            moods.append(mood.__dict__)

    return json.dumps(moods)
from models import Mood

def get_single_mood(id):
    with sqlite3.connect('../../dailyjournal.db') as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            m.id,
            m.label
        FROM moods m
        WHERE m.id = ?
        """, (id, ))

        moods = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            mood = Mood(row['id'], row['label'])

            moods.append(mood.__dict__)

    return json.dumps(moods)


def delete_mood(id):
    with sqlite3.connect('../../dailyjournal.db') as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM moods
        WHERE id = ?
        """, (id, ))


