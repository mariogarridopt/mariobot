import json
import time
import os

DATA_FILE = "voice_data.json"

# users currently in voice
active_sessions = {}


def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)


def user_join(user_id):
    active_sessions[user_id] = time.time()


def user_leave(user_id):
    if user_id not in active_sessions:
        return

    join_time = active_sessions.pop(user_id)
    session_time = int(time.time() - join_time)

    data = load_data()

    user_id = str(user_id)

    if user_id not in data:
        data[user_id] = 0

    data[user_id] += session_time

    save_data(data)


def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{hours}h {minutes}m"


def top_list(guild, limit=10):
    data = load_data()

    if not data:
        return "No voice activity recorded yet."

    sorted_users = sorted(data.items(), key=lambda x: x[1], reverse=True)

    result = "**🎤 Voice Leaderboard**\n\n"

    for i, (user_id, seconds) in enumerate(sorted_users[:limit], start=1):
        member = guild.get_member(int(user_id))
        name = member.display_name if member else f"User {user_id}"

        result += f"{i}. {name} — {format_time(seconds)}\n"

    return result

def user_time(guild, user):
    data = load_data()

    user_id = str(user.id)

    if user_id not in data:
        return f"{user.display_name} has no recorded voice time."

    total_seconds = data[user_id]

    return f"🎤 {user.display_name} has spent **{format_time(total_seconds)}** in voice channels."
