from typing import Optional
import discord
from discord.ext import commands
import os
import modules.roll as roll
import modules.voicerank as rank

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
        GUILD_ID = 811639406704066621
        guild = discord.Object(id=GUILD_ID)
        synced_commands = await client.tree.sync(guild=guild)
        #synced_commands = await client.tree.sync()
        print(f'{str(len(synced_commands))} commands synced')

        # Up and ready to go
        print(f'{client.user} is running!')


    @client.event
    async def on_voice_state_update(member, before, after):
        SUFIX = "¡channel!"
        CHANNEL_ID = 1148277892351000627

        # Track voice time
        if before.channel is None and after.channel is not None:
            rank.user_join(member.id)

        elif before.channel is not None and after.channel is None:
            rank.user_leave(member.id)
        
        # when a member join a voice channel = CHANNEL_ID
        if after.channel and after.channel.id == CHANNEL_ID:
            new_channel = await after.channel.guild.create_voice_channel(f'{member.name} {SUFIX}', category=after.channel.category)
            await member.move_to(new_channel)

        # when a member leaves a voice channel ending with SUFIX
        if before.channel and len(before.channel.members) < 1:
            if before.channel.name.endswith(SUFIX):
                await before.channel.delete()


    # available commands
    @client.tree.command(name="roll", description="Test your luck, role a number between 1 and 10")
    async def roll_int(interaction: discord.Interaction):
        res = roll.role_int()
        await interaction.response.send_message(content=res)
    
    @client.tree.command(name="topvoice", description="Rank of time spent in voice channels")
    async def topvoice(interaction: discord.Interaction):
        res = rank.top_list(interaction.guild)
        await interaction.response.send_message(content=res)

    @client.tree.command(name="voicetime", description="Show how much time a user has spent in voice channels")
    async def voicetime(interaction: discord.Interaction, user: discord.Member):
        res = rank.user_time(interaction.guild, user)
        await interaction.response.send_message(content=res)

    client.run(TOKEN)
