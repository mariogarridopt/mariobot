import time
from discord.ext import tasks, commands

class TimerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.index = 0
        self.printer.start()

    def cog_unload(self):
        self.printer.cancel()

    @tasks.loop(minutes=10)
    async def printer(self):
        timeBending = time.time() + 300
        displayTime = time.strftime("%I:%M %p", time.localtime(timeBending))
        await self.bot.get_channel(1097001611479498793).edit(name= ("⏰ ~ " + displayTime))
        self.index += 1

