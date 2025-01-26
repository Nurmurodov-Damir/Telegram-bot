async def check_subscription(user_id, bot, channels):
    for channel in channels:
        member = await bot.get_chat_member(channel, user_id)
        if member.status not in ["member", "administrator", "creator"]:
            return False
    return True
