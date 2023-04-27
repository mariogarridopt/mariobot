import pytz
from datetime import datetime
from datetime import timedelta
from discord.ext import tasks, commands

class timer_cog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.index = 0
        self.printer.start()

    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(minutes=10)
    async def printer(self):
        displayTime = timer_cog.getCurretTime()
        await self.bot.get_channel(1097001611479498793).edit(name= ("⏰ ~ " + displayTime))
        self.index += 1

    @staticmethod
    def getCurretTime():
        portugal_timezone = pytz.timezone('Europe/Lisbon')
        current_time = datetime.now(portugal_timezone)
        current_time = current_time + timedelta(minutes=5)

        return current_time.strftime("%I:%M %p")