from base64 import b64decode

tokenfile = open('TOKEN', 'r')
__THING__ = tokenfile.read()
__THING__ = b64decode(__THING__).decode('utf-8')

import discord
from discord.ext import commands
from random import randint

intents = discord.Intents.all()
messages = ['uwu', 'x3', ':3', 'rawr']
real_spellings = ['real', 'rael', 'rail', 'rewal',
                  'ral', 'rea', 'rel', 'rl', 'rela',
                  'rale', 'relea', 'rele', 'rala',
                  'eal', 'rewel']

bot =  commands.Bot(command_prefix='$',intents=intents)

@bot.event
async def on_message(message):
    if message.author.id == 973943523655164032:
        if(message.content == 'kiss boyfie' or message.content == 'kiss awest' or message.content == 'kiss awext'):
            await message.channel.send("*kisses* <@590880459660066818> " + messages[randint(0, 3)])


        if(message.content == 'i wuv boyfie' or message.content == 'i wuv awest' or message.content == 'i wuv awext'):
            await message.channel.send("i wuv you <@590880459660066818> " + messages[randint(0, 3)])


        if(message.channel.id == 1115319072314372177 and 'rate' in message.content):
            await message.channel.send("<@590880459660066818> " + messages[randint(0, 3)])


        if(message.content in real_spellings):
            try:
                await message.delete()
                await message.channel.send("# stop playing real <@973943523655164032>")
            except Exception:
                await message.channel.send("who took my permission grr")

        if((message.content.lower()).strip('!@#$%^&*(){}|:"<>?\'1234567890-=[]\;,./') in 'hihellohellphii'):
            await message.reply('hi')

        if((message.content.lower()).strip('!@#$%^&*(){}|:"<>?\'1234567890-=[]\;,./') == 'cherry'):
            await message.reply('uwu')

        if(message.content == 'your mom'):
            await message.reply('insane burn')

bot.run(__THING__)
