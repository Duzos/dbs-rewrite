# Imports
from discord.interactions import InteractionMessage
import interactions
import json

# Setting up the bot

with open('config.json', 'r') as f:
    config = json.load(f)

token = config['token']

bot = interactions.Client(token=token)

@bot.event
async def on_ready():
    print("bot is ready.")

# Commands



 # Information Category

@bot.command(name='information',description='Sends info on the bot.')
async def _information(ctx):
    embed = interactions.Embed(title='discord-interactions | python',description='by <@!327807253052653569>\n[Github Page](https://github.com/Duzos/DuBot-Slash)\n[Support Server](https://discord.gg/Raakw6367z)')

@bot.command(type=interactions.ApplicationCommandType.USER,name='Get Avatar')
async def _getavatar(ctx: interactions.CommandContext):
    embed = interactions.Embed(title=f'{ctx.target.username}\'s Avatar',image=interactions.EmbedImageStruct(url=f'https://cdn.discordapp.com/avatars/{ctx.target.id}/{ctx.target.avatar}')._json,color=ctx.target.accent_color)
    await ctx.send(embeds=[embed])

# Tests
@bot.command(name='test',description='simple test command for interactions library',scope=862066219774902313)
async def _test(ctx):
    await ctx.send("HI")
    embed = interactions.Embed(title='embed test',description='test',author=interactions.EmbedAuthor(name='Name')._json,thumbnail=interactions.EmbedImageStruct(url="https://cdn.discordapp.com/attachments/827389916894724099/923323428323348590/IMG_5706.png")._json,fields=[interactions.EmbedField(name='field 1',value='field 1 value')._json],footer=interactions.EmbedFooter(text='footer')._json,color=0xff0000)
    button = interactions.Button(style=interactions.ButtonStyle.PRIMARY,label='I AM A BUTTON',custom_id='test_button')
    await ctx.send(embeds=[embed], components=button)

@bot.command(type=interactions.ApplicationCommandType.USER,name='context menu test',scope=862066219774902313)
async def _contexttest(ctx):
    await ctx.send(f"You used a context menu on <@!{ctx.target.id}>!")

bot.start()
