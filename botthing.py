# imports
from base64 import b64decode
import discord
from discord.ext import commands
from random import randint
from pathlib import Path
import json

datapath = str(Path(__file__).parent.resolve()) + '/data.json'

usrdatafile = open(datapath, 'r')
usrdata = json.load(usrdatafile)


# reading data
__THING__ = usrdata["token"]
sheryel = usrdata["sheryel"]
awex = usrdata["awex"]
mushrooms = int(usrdata["mushrooms"])

messages = ['uwu', 'x3', ':3', 'rawr']
real_spellings = ['real', 'rael', 'rail', 'rewal',
                  'ral', 'rea', 'rel', 'rl', 'rela',
                  'rale', 'relea', 'rele', 'rala',
                  'eal', 'rewel']

intents = discord.Intents.all()

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_message(message):
    json.dump(usrdata, usrdatafile)
    if not message.author.id == 1115615704071282750:
        if message.author.id == sheryel:

            # kiss dear awex
            if(message.content == 'kiss boyfie' or message.content == 'kiss awest' or message.content == 'kiss awext'):
                await message.channel.send("*kisses* <@" + str(awex) + "> " + messages[randint(0, 3)])

            # i wuv boyfie
            if(message.content == 'i wuv boyfie' or message.content == 'i wuv awest' or message.content == 'i wuv awext' or message.content == 'wuv awext' or message.content == 'wuv awest' or message.content == 'wuv boyfie'):
                await message.channel.send("i wuv you <@" + str(awex) + "> " + messages[randint(0, 3)])

            if message.content == 'eep' or message.content == 'sleep' or message.content == 'sleepy':
                await message.channel.send("i eep <@" + str(awex) + "> " + messages[randint(0, 3)])

            # pings awex in rate song channel when a sentence with the word rate is used
            if(message.channel.id == 1115319072314372177 and 'rate' in message.content):
                await message.channel.send("<@" + str(awex) + "> " + messages[randint(0, 3)])

            # sheryel real preventer
            if(message.content in real_spellings):
                await message.delete()
                await message.channel.send("# stop playing real <@" + str(sheryel) + ">")

            # says hi when stuff
            if((message.content.lower()).strip('!@#$%^&*(){}|:"<>?\'1234567890-=[]\;,./') in ['hi', 'hello', 'hellp', 'hii']):
                await message.reply('hi')

            # says something in messages when cherry is mentioned
            if((message.content.lower()).strip('!@#$%^&*(){}|:"<>?\'1234567890-=[]\;,./') == 'cherry'):
                await message.reply(messages[randint(0, 3)])

            # your mom
            if(message.content == 'your mom'):
                await message.reply('insane burn')
        
        if message.author.id == 1114730963600150528 and message.content == 'no' and message.channel.id == 1115319072314372177:
            await message.delete()
            await message.channel.send("<@" + str(awex) + "> " + messages[randint(0, 3)])

        if message.content == "🍄":
            await message.reply('mushroom')
            mushrooms += + 1
            usrdata["mushrooms"] = mushrooms
        
        if message.content == "mushrooms":
            await message.channel.send(str(mushrooms) + "mushrooms")




bot.run(__THING__)