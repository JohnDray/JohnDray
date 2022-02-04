import dadjokes
import keep_alive
import discord
import os
from discord.ext import commands
from discord import Member
from discord.ext import commands
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions, CheckFailure
import random
from replit import db
from PIL import Image
import requests

client = discord.Client()
client = commands.Bot(command_prefix=['j;', 'J;'], help_command=None)

quote1 = 'id rather fuck a horse than look at your face.'
quote2 = 'i cant think of something nice of you because you make me wanna puke... have a nice day!'
quote3 = 'No one likes you so you have to pick a quote from here, lonely bitch!'
quote4 = 'Ran into an error. This happened because your a dick. Stop using the quotes command dumbass.'
quote5 = 'Your so ugly that your face ruins my day!'
quote6 = " Here's a tip: dont leave your mom's room door open for me next time."
quotelist = [quote1, quote2, quote3, quote4, quote5, quote6]


@client.command(aliases=['clist'])
async def help(ctx):
  embed = discord.Embed(title="Here's the list for commands",
                         description="""**Fun**:
- dadjoke | Description: Sends a random dad joke. | Aliases: Dadjoke, dje
- topquotes | Description : Sends a random one of the best quotes. | Aliases: None
- say | Description: allows you to say something within the bot
- swearat | Description: Swears at somebody using a random cuss word | Aliases: none
- quote | Description: Gives you a very *inspirational* quote | Aliases: none
- quoteto | Description: Shares a quote to somebody. | Aliases: none

**Admin/Moderator**:
- clearall | Description: Deletes all messages within a channel, requires the permission: manage messages | Aliases: Clearall, purge, Purge

**Misc**: 
Help | Description: triggers the help list | Aliases: clist

""", color=0xFF00)
  embed.add_field(name="DISCLAIMER:", value="This bot is still in development, many more commands is planned!", inline=False)
  await ctx.send(embed=embed)

@client.command()
async def t(ctx):
    await ctx.send('working lel')


@client.command(aliases=['Dadjoke', 'dje'])
async def dadjoke(ctx):
    funny = dadjokes.joke()
    embed = discord.Embed(title="Here's a dad joke lol",
                          description=funny,
                          color=0xFF00)
    await ctx.send(embed=embed)


@client.command()
async def who1sdev(ctx, mention):
    embed = discord.Embed(title=f'ID: {ctx.message.mention.id}',
                          description=f'The id of this user is {mention.id}',
                          colour=discord.Colour.blue())
    embed.set_footer(text=f'called by {ctx.message.author}')
    embed.set_image(ctx.mention.avatar_url)
    embed.set_author(name=f'{ctx.message.mention}',
                     icon_url=ctx.author.avatar_url)
    await ctx.channel.message.send(embed=discord.embed)


@client.command()
async def topquotes(ctx):
    topquote1 = 'this bot is the best yet - *JohnDray#5137'
    topquote2 = 'This bot is so good - *JohnDray#5137*'
    topquotes = [topquote1, topquote2]
    await ctx.send(
        f'''Heres a random quote {ctx.message.author.mention}: "{random.choice(topquotes)}"'''
    )


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.send(
            "Thats not even a command!! Use **j;clist** for commands!")


@client.command(aliases=['Say'])
async def say(ctx, *, message):
    await ctx.message.delete()
    await ctx.send(message)


@client.command(name="clearall", aliases=['Clearall', 'purge', 'Purge'])
@has_permissions(manage_messages=True)
async def clearall(ctx):
    await ctx.channel.purge()
    await ctx.send("All messages has been deleted in this channel.")


@client.command()
async def swearat(ctx, mention):

    swear1 = f"{mention} you are a poopoohead!"
    swear2 = f"{mention}, you are a dick head!"
    swear3 = f"{mention}, you dick!"
    swear4 = f"{mention}, you should go fuck yourself"
    swear5 = f"{mention}, you are a bitch"
    swear6 = f"{mention}, you mother fucker!"
    swear7 = f"{mention}, you are a pussssy!!!"
    swear8 = f"{mention}, you bastard!"

    swearinglist1 = [
        swear1, swear2, swear3, swear4, swear5, swear6, swear7, swear8
    ]

    await ctx.message.delete()
    await ctx.send(
        f"{ctx.message.author.mention} has said to, {random.choice(swearinglist1)}"
    )


@client.command()
async def quote(ctx):
    await ctx.send(random.choice(quotelist))


@client.command()
async def invbot2urserver(ctx):
    await ctx.send(
        'Heres the invite link cant wait to join uwu: https://discord.com/api/oauth2/authorize?client_id=890202659099926530&permissions=8&scope=bot'
    )


@client.command()
async def quoteto(ctx, mention):
    await ctx.send(
        f"heres a quote for: {mention} \n\n {random.choice(quotelist)}")


@client.event
async def on_ready():
    await client.change_presence(
        status=discord.Status.idle,
        activity=discord.Activity(
            type=discord.ActivityType.playing,
            name="ur mom",
            url="https://www.youtube.com/watch?v=dQw4w9WgXcQ"))
    print('We have logged in as {0.user}'.format(client))


keep_alive.keep_alive()
client.run(os.environ['TOKEN'])
