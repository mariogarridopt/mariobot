import time

# users currently in voice
active_sessions = {}

# total voice time stored in memory
voice_totals = {}


def user_join(user_id):
    active_sessions[user_id] = time.time()


def user_leave(user_id):
    if user_id not in active_sessions:
        return

    join_time = active_sessions.pop(user_id)
    session_time = int(time.time() - join_time)

    if user_id not in voice_totals:
        voice_totals[user_id] = 0

    voice_totals[user_id] += session_time

    #debug
    print(
        f"[VOICE TRACK] User {user_id} gained {format_time(session_time)} "
        f"(total: {format_time(voice_totals[user_id])})"
    )


def format_time(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    return f"{hours}h {minutes}m"


def top_list(guild, limit=10):
    if not voice_totals:
        return "No voice activity recorded yet."

    sorted_users = sorted(voice_totals.items(), key=lambda x: x[1], reverse=True)

    result = "**🎤 Voice Leaderboard**\n\n"

    for i, (user_id, seconds) in enumerate(sorted_users[:limit], start=1):
        member = guild.get_member(user_id)
        name = member.display_name if member else f"User {user_id}"

        result += f"{i}. {name} — {format_time(seconds)}\n"

    return result


def user_time(guild, user):
    user_id = user.id

    if user_id not in voice_totals:
        return f"{user.display_name} has no recorded voice time."

    total_seconds = voice_totals[user_id]

    return f"🎤 {user.display_name} has spent **{format_time(total_seconds)}** in voice channels."
