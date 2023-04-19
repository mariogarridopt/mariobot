import discord
from discord.ext import commands
from modules.timer_cog import timer_cog
from modules.music_cog import music_cog
import modules.react as react
import os
import modules.roll as roll

def run_discord_bot():
    TOKEN = os.getenv('BOT_TOKEN', '')
    if TOKEN == '':
        print('Please provide a token to this bot...')
        return
    
    intents = discord.Intents.default()
    intents.message_content = True
    intents.reactions = True
    intents.members = True
    intents.voice_states = True

    client = commands.Bot(command_prefix="!", intents = intents)

    @client.event
    async def on_ready():
        # Command sync
        synced_commands = await client.tree.sync()
        print(f'{str(len(synced_commands))} commands synced')
        
        # Timer cog start
        timer_cog(client)
        print('Timer COG Started!')

        # Up and ready to go
        print(f'{client.user} is running!')

    # react to message events
    @client.event
    async def on_raw_reaction_add(payload):
        await react.role_on_react(
            payload.message_id,
            payload.emoji,
            payload.member,
            True
        )

    @client.event
    async def on_raw_reaction_remove(payload):
        guild = client.get_guild(payload.guild_id)
        member = discord.utils.get(guild.members, id=payload.user_id)
        
        await react.role_on_react(
            payload.message_id,
            payload.emoji,
            member,
            False
        )

    # available commands
    @client.tree.command(name="roll", description="Test your luck, role a number between 1 and 10")
    async def roll_int(interaction: discord.Interaction):
        res = roll.role_int()
        await interaction.response.send_message(content=res)
    
    @client.tree.command(name="valorantroll", description="Let me pick an agent for you")
    async def roll_valorant(interaction: discord.Interaction):
        res = roll.role_valorant()
        await interaction.response.send_message(content='You are going to play ' + res)

    @client.tree.command(name="leagueroll", description="Let me pick a champion for you")
    @discord.app_commands.autocomplete(lane=roll.lane_autocomplete)
    async def roll_league(interaction: discord.Interaction, lane: str):
        res = roll.role_legueoflegends(lane)
        await interaction.response.send_message(content='You are going to play ' + res)

    @client.tree.command(name="leagueroll_random", description="Let me pick a champion for you")
    async def roll_league_randomLane(interaction: discord.Interaction):
        res = roll.role_legueoflegends("")
        await interaction.response.send_message(content='You are going to play ' + res)
    
    client.run(TOKEN)