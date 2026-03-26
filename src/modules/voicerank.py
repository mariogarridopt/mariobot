import json
import time
import os

# Path to save voice data
DATA_FILE = "voice_data.json"

# In-memory tracking of active sessions
active_sessions = {}

# Load persisted data
def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            print("[VOICE DATA] JSON file corrupted. Resetting data.")
            return {}

# Save data to file
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

# Called when user joins voice
def user_join(user_id):
    active_sessions[user_id] = time.time()
    print(f"[VOICE TRACK] User {user_id} joined voice.")

# Called when user leaves voice
def user_leave(user_id):
    if user_id not in active_sessions:
        return

    join_time = active_sessions.pop(user_id)
    session_time = int(time.time() - join_time)

    data = load_data()

    user_id_str = str(user_id)
    if user_id_str not in data:
        data[user_id_str] = 0

    data[user_id_str] += session_time
    save_data(data)

    print(
        f"[VOICE TRACK] User {user_id} gained {format_time(session_time)} "
        f"(total: {format_time(data[user_id_str])})"
    )

# Format seconds into hours and minutes
def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{hours}h {minutes}m"

# Return top voice users as a leaderboard
def top_list(guild, limit=10):
    if not guild:
        return "Error: Guild not provided."

    data = load_data()
    if not data:
        return "No voice activity recorded yet."

    # Include ongoing sessions
    for user_id, join_time in active_sessions.items():
        user_id_str = str(user_id)
        session_time = int(time.time() - join_time)
        if user_id_str in data:
            data[user_id_str] += session_time
        else:
            data[user_id_str] = session_time

    sorted_users = sorted(data.items(), key=lambda x: x[1], reverse=True)
    result = "**🎤 Voice Leaderboard**\n\n"

    for i, (user_id_str, seconds) in enumerate(sorted_users[:limit], start=1):
        try:
            user_id_int = int(user_id_str)
            member = guild.get_member(user_id_int)
            name = member.display_name if member else f"User {user_id_str}"
        except:
            name = f"User {user_id_str}"

        result += f"{i}. {name} — {format_time(seconds)}\n"

    return result

# Return total voice time for a specific user
def user_time(guild, user):
    if not guild or not user:
        return "Error: Guild or user not provided."

    data = load_data()
    user_id_str = str(user.id)
    total_seconds = data.get(user_id_str, 0)

    # Include current session if user is in voice
    if user.id in active_sessions:
        total_seconds += int(time.time() - active_sessions[user.id])

    if total_seconds == 0:
        return f"{user.display_name} has no recorded voice time."

    return f"🎤 {user.display_name} has spent **{format_time(total_seconds)}** in voice channels."
