import time
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
        timeBending = time.time() + 300
        displayTime = time.strftime("%I:%M %p", time.localtime(timeBending))
        return displayTime
