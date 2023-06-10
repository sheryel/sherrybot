# imports
import discord
from discord.ext import commands, tasks
from random import randint, choice, random
from pathlib import Path
import json
from shutil import copyfile
from re import sub

datapath = f'{Path(__file__).parent.resolve()}/data.json'
backuppath = f'{Path(__file__).parent.resolve()}/.backupdata'

with open(datapath, 'r+') as usrdatafile:
    usrdata = json.load(usrdatafile)

__TOKEN__ = str(usrdata["token"])
sheryel = int(usrdata["sheryel"])
awex = int(usrdata["awex"])
mushrooms = int(usrdata["mushrooms"])

messages = ('uwu', 'x3', ':3', 'rawr')
real_spellings = {
    'real', 
    'rael', 
    'rail', 
    'rewal',
    'ral', 
    'rea', 
    'rel', 
    'rl', 
    'rela',
    'rale', 
    'relea', 
    'rele', 
    'rala',
    'eal', 
    'rewel'
}

kiss = {
    'kiss boyfie', 
    'kiss awest', 
    'kiss awext'
}
wuv = {
    'i wuv boyfie', 
    'wuv boyfie', 
    'i wuv awest', 
    'i wuv awext', 
    'wuv awest', 
    'wuv awext', 
}

awestpings = (
    f"hewwo <@{awex}>", 
    f"hewwo <@{awex}> {messages[randint(0, 3)]}", 
    f"<@{awex}> wuv you {messages[randint(0, 3)]}", 
    f"<@{awex}> wuv you", 
    f"<@{awex}> {messages[randint(0, 3)]}",
    f"*kisses* <@{awex}> {messages[randint(0, 3)]}",
    f"*kisses* <@{awex}>"
)

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='$', intents=intents)


def backup():
    copyfile(backuppath, datapath)

def normalize_message(content):
    return sub(r'[^\w\s]', '', content.strip().lower())

def writedata():
    with open(datapath, 'w') as usrdatafile:
        usrdatafile.truncate(0)
        json.dump(usrdata, usrdatafile)


@bot.event
async def on_message(message):
    normalizedcontent = normalize_message(message.content)

    if message.author.id == sheryel and not message.author.id == 1115615704071282750:

        if normalizedcontent in kiss:
            await message.channel.send(f"*kisses* <@{awex}> {messages[randint(0, 3)]}")
        
        elif normalizedcontent in wuv:
            await message.channel.send(f"i wuv you <@{awex}> {messages[randint(0, 3)]}")

        # if message.content == 'eep' or message.content == 'sleep' or message.content == 'sleepy':
        elif message.content in {'eep', 'eepy', 'sleep', 'sleepy'}:
            await message.channel.send("i eep <@" + str(awex) + "> " + messages[randint(0, 3)])

        # pings awex in rate song channel when a sentence with the word rate is used
        elif message.channel.id == 1115319072314372177 and 'rate' in message.content:
            await message.channel.send("<@" + str(awex) + "> " + messages[randint(0, 3)])

        # sheryel real preventer
        elif message.content in real_spellings:
            await message.delete()
            await message.channel.send("# stop playing real <@" + str(sheryel) + ">")

        # says hi when stuff
        elif normalizedcontent in {'hi', 'hello', 'hellp', 'hii'}:
            await message.reply('hi')

        # says something in messages when cherry is mentioned
        elif normalizedcontent == 'cherry':
            await message.reply(messages[randint(0, 3)])

        # your mom
        elif message.content == 'your mom':
            await message.reply('insane burn')

    elif message.author.id == 1114730963600150528 and message.content == 'no' and message.channel.id == 1115319072314372177:
        await message.delete()
        await message.channel.send("<@" + str(awex) + "> " + messages[randint(0, 3)])

    elif message.content == "🍄":
        await message.reply('mushroom')
        mushrooms += + 1
        usrdata["mushrooms"] = mushrooms
        writedata()

    elif message.content == "mushrooms":
        await message.channel.send(f'{mushrooms} mushrooms')

@tasks.loop(minutes=0.5)
async def pingawex():
    if random < 0.005:
        channel = bot.get_channel(1112322137554960465)
        await channel.send(choice(awestpings))




bot.run(__TOKEN__)