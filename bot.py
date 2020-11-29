# bot.py
import os
import random
import discord
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')          

bot = commands.Bot(command_prefix='!')
bot.remove_command(('help'))

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Brooklyn 99| !help"))

@bot.command(name='99')
async def nine_nine(ctx):
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        'Title of your sex tape',
        'Sarge, with all due respect, I am gonna completely ignore everything you just said',
        'The English language can not fully capture the depth and complexity of my thoughts, so I’m incorporating emojis into my speech to better express myself. Winky face',
        'A place where everybody knows your name is hell. You’re describing hell',
        'Cool, cool, cool, cool, cool. No doubt, no doubt, no doubt',
        'If I die, turn my tweets into a book',
        'Great, I’d like your $8-est bottle of wine, please.',
        'Fine. but in protest, I’m walking over there extremely slowly!',
        'Jake, why don’t you just do the right thing and jump out of a window?',
        'I asked them if they wanted to embarrass you, and they instantly said yes',
        'Captain Wuntch. Good to see you. But if you’re here, who’s guarding Hades?',
        'I’m playing Kwazy Cupcakes, I’m hydrated as hell, and I’m listening to Sheryl Crow. I’ve got my own party going on',
        'Anyone over the age of six celebrating a birthday should go to hell',
        'Captain, turn your greatest weakness into your greatest strength. Like Paris Hilton RE: her sex tape',
        'Okay, no hard feelings, but I hate you. Not joking. Bye.',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    response = random.choice(brooklyn_99_quotes)
    await ctx.send(response)

@bot.command(name='help')
async def help(ctx):
    embed = discord.Embed(title="Brooklyn99 Bot", colour=discord.Colour(0x98df6e), url="https://github.com/dhruvjha11/Brooklyn99-Bot", description="Vote us on\n[Top.gg](https://top.gg/bot/781444535389126666) | [BFD](https://botsfordiscord.com/bot/781444535389126666)\n[Support Server](https://discord.gg/Ed9vvZrScN)\n[Invite the Bot](https://discord.com/api/oauth2/authorize?client_id=781444535389126666&permissions=19520&scope=bot)")

    embed.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/0.png")
    embed.set_author(name="Dhruv Jha", url="https://github.com/dhruvjha11", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
    embed.set_footer(text="Any Issues? Join Support Server", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")

    embed.add_field(name="!99", value="Returns a quote from Brooklyn 99", inline=False)
    embed.add_field(name="Developer:", value="Dhruv Jha", inline=True)
    embed.add_field(name="Date Released:", value="26-Nov-2020", inline=True)
    embed.add_field(name="Servers:", value= f" {str(len(bot.guilds))}")
    await ctx.send(embed=embed)
bot.run(TOKEN)
