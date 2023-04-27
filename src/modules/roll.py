import random
from typing import List
import discord

LEAGUE_POSITIONS = ['top', 'jungle', 'mid', 'adc', 'support']
LEAGUE_CHAMPIONS = {
    'top': ['Aatrox', 'Camille', 'Darius', 'Dr. Mundo', 'Fiora', 'Garen', 'Gangplank', 'Gnar', 'Irelia', 'Jax', 'Jayce', 'Kennen', 'Kled', 'Malphite', 'Maokai', 'Mordekaiser', 'Nasus', 'Ornn', 'Pantheon', 'Poppy', 'Quinn', 'Renekton', 'Riven', 'Sett', 'Shen', 'Singed', 'Sion', 'Teemo', 'Trundle', 'Tryndamere', 'Urgot', 'Vladimir', 'Volibear', 'Wukong', 'Yorick'],
    'jungle': ['Amumu', 'Camille', 'Elise', 'Evelynn', 'Fiddlesticks', 'Gragas', 'Graves', 'Hecarim', 'Ivern', 'Jarvan IV', 'Jax', 'Karthus', 'Kayn', 'Kindred', 'Kha\'Zix', 'Lee Sin', 'Master Yi', 'Nidalee', 'Nocturne', 'Nunu & Willump', 'Olaf', 'Rammus', 'Rek\'Sai', 'Rengar', 'Sejuani', 'Shaco', 'Skarner', 'Taliyah', 'Trundle', 'Udyr', 'Vi', 'Volibear', 'Warwick', 'Wukong', 'Xin Zhao', 'Zac'],
    'mid': ['Ahri', 'Akali', 'Anivia', 'Annie', 'Aphelios', 'Aurelion Sol', 'Azir', 'Brand', 'Cassiopeia', 'Corki', 'Diana', 'Ekko', 'Fizz', 'Galio', 'Heimerdinger', 'Irelia', 'Jayce', 'Kassadin', 'Katarina', 'LeBlanc', 'Lissandra', 'Lucian', 'Malphite', 'Malzahar', 'Neeko', 'Orianna', 'Qiyana', 'Rumble', 'Ryze', 'Sylas', 'Syndra', 'Talon', 'Twisted Fate', 'Veigar', 'Vel\'Koz', 'Viktor', 'Vladimir', 'Xerath', 'Yasuo', 'Yone', 'Zed', 'Zoe'],
    'adc': ['Aphelios','Ashe','Caitlyn','Draven','Ezreal','Graves','Jhin','Jinx','Kalista','Kog\'Maw','Lucian','Miss Fortune','Samira','Senna','Seraphine','Sivir','Tristana','Twitch','Varus','Vayne','Xayah'],
    'support': ['Alistar','Bard','Blitzcrank','Brand','Braum','Fiddlesticks','Galio','Janna','Karma','Leona','Lulu','Lux','Morgana','Nami','Nautilus','Pantheon','Pyke','Rakan','Senna','Seraphine','Sona','Soraka','Swain','Taric','Thresh','Vel\'Koz','Xerath','Yuumi','Zilean']
}
LEAGUE_BUILDS = ['full ap', 'full ad', 'hybrid ap/ad', 'tank', 'bruiser', 'assassin']
VAL_CHAR_NAMES = ['Brimstone', 'Sage', 'Sova', 'Viper', 'Cypher', 'Phoenix',
    'Jett', 'Raze', 'Reyna', 'Killjoy', 'Skye', 'Yoru', 'Astra', 'KAY/O']

def role_int() -> int:
    return random.randint(1, 10)

def role_valorant() -> str:
    return VAL_CHAR_NAMES[random.randint(0, len(VAL_CHAR_NAMES) - 1)]

def role_legueoflegends(lane) -> str:
    if(lane.lower() not in LEAGUE_POSITIONS):
        lane = LEAGUE_POSITIONS[random.randint(0, len(LEAGUE_POSITIONS) - 1)]

    champList = LEAGUE_CHAMPIONS[lane.lower()]

    randBuildIndex = random.randint(0, len(LEAGUE_BUILDS) - 1)
    pickedBuild = LEAGUE_BUILDS[randBuildIndex]

    randChampIndex = random.randint(0, len(champList) - 1)
    pickedChamp = champList[randChampIndex]

    return lane + ' - ' + pickedChamp + ' - ' + pickedBuild

async def lane_autocomplete(
    interaction: discord.Interaction,
    current: str,
) -> List[discord.app_commands.Choice[str]]:
    return [
        discord.app_commands.Choice(name=lane, value=lane)
        for lane in LEAGUE_POSITIONS if current.lower() in lane.lower()
    ]