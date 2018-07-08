# Melobot by Melo

import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.bot(command_prefix='+')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello, there!")

@bot.command()
async def info (ctx, user: discord.Member):
     await bot.say("The users name is: {}".format(user.name))
     await bot.say("The users ID is: {}".format(user.id))
     await bot.say("The users status is: {}".fomat[user.status])
     await bot.say("The user joined at: {}".format(user.joined_at))
    
bot.run('<NDY1NTQ1MjE2MDIwMDU0MDE2.DiPEaA.ah0AF29GfuJjT8g6L_5JS5Si5MU>')
