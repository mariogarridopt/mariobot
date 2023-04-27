import discord

async def role_on_react(message_id, emoji, member, add) -> None:
    print(f'{member}: reacted with {emoji} to {message_id}')
    if(str(message_id) == '811657538391113788' and str(emoji) == '✅'):
        role_name = 'Crowd'
        role = discord.utils.get(member.guild.roles, name=role_name)
        if(add):
            await member.add_roles(role)
            print(f'{role_name} role added to {member}')
        else:
            await member.remove_roles(role)
            print(f'{role_name} role removed from {member}')

    elif str(message_id) == '812511925669724171':
        if str(emoji) == '🏹':
            role_name = 'Minecraft'
        elif str(emoji) == '🔫':
            role_name = 'Rust'
        elif str(emoji) == '🏆':
            role_name = 'League Of Legends'
        elif str(emoji) == '💣':
            role_name = 'Valorant'
        elif str(emoji) == '🏰':
            role_name = 'Fortnite'
        else:
            role_name = ''

        if(role_name != ''):
            role = discord.utils.get(member.guild.roles, name=role_name)
            if(add):
                await member.add_roles(role)
                print(f'{role_name} role added to {member}')
            else:
                await member.remove_roles(role)
                print(f'{role_name} role removed from {member}')
