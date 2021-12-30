import discord
import datetime
import os
from discord.ext import commands


client = discord.Client()

intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)

bot = commands.Bot(command_prefix="",intents=intents)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for Improvements"))

@bot.command(name="add.cog")    #ajoute un cog
async def addcog(ctx, extension):
    if True: #----------------------PERMISSIONS A AJOUTER--------------------------------------------------------------
        bot.load_extension(f"cogs.{extension}")
        embed = discord.Embed(title=f"Activation du COG {extension}", description="Activation réussie", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
        embed.set_footer(text=f"Demandée par {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Vous n'avez pas la permission pour effectuer cette action...")

@bot.command(name="remove.cog") #retire un cog
async def removecog(ctx,extension):
    if True: #----------------------PERMISSIONS A AJOUTER--------------------------------------------------------------
        bot.unload_extension(f"cogs.{extension}")
        embed = discord.Embed(title=f"Désactivation du COG {extension}", description="Désactivation réussie", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
        embed.set_footer(text=f"Demandée par {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Vous n'avez pas la permission pour effectuer cette action...")


@bot.command(name="reload.cog") #recharge un cog
async def reloadcog(ctx,extension):
    if True: #----------------------PERMISSIONS A AJOUTER--------------------------------------------------------------
        bot.unload_extension(f"cogs.{extension}")
        bot.load_extension(f"cogs.{extension}")
        embed = discord.Embed(title=f"Rechargement du COG {extension}", description="Rechargement réussi", timestamp=datetime.datetime.utcnow(), color=discord.Color.red())
        embed.set_footer(text=f"Demandé par {ctx.author.display_name}",icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)
    else:
        await ctx.send("Vous n'avez pas la permission pour effectuer cette action...")

@bot.event #Supprime les erreurs dans l'invit de commande
async def on_command_error(ctx, exception):
    error = getattr(exception, "original", exception)
    if type(error) == commands.errors.CommandNotFound:
        return
    else:
        raise error

for filename in os.listdir("./cogs"):       #Active les cogs au lancement
    if filename.endswith('.py'):
        bot.load_extension(f"cogs.{filename[:-3]}")

bot.run("PLACE TOKEN HERE")