import json
import os

LEADERBOARD_FILE = "leaderboard.json"
SETTINGS_FILE = "settings.json"


def load_leaderboard():
    if not os.path.exists(LEADERBOARD_FILE):
        return []
    with open(LEADERBOARD_FILE, "r") as f:
        return json.load(f)


def save_leaderboard(data):
    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_score(name, score, distance):
    data = load_leaderboard()
    data.append({
        "name": name,
        "score": score,
        "distance": int(distance)
    })
    data = sorted(data, key=lambda x: x["score"], reverse=True)[:10]
    save_leaderboard(data)


def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        return {
            "sound": True,
            "difficulty": "medium",
            "car_color": "default"
        }
    with open(SETTINGS_FILE, "r") as f:
        return json.load(f)


def save_settings(settings):
    with open(SETTINGS_FILE, "w") as f:
        json.dump(settings, f, indent=4)