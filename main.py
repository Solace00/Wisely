import discord
import os
import random
from discord.ext import commands


bot = commands.Bot(command_prefix = '-')
bot.remove_command('help')

#@bot.event()
#async def on_ready():
#    print(f"bot is ready")

@bot.command()
async def load(ctx, extension):
    bot.load_extension(f'Cogs.{extension}')

async def unload(ctx, extension):
    bot.unload_extension(f'Cogs.{extension}')

for filename in os.listdir('./Cogs'):
        if filename.endswith('.py'):
                bot.load_extension(f'Cogs.{filename[:-3]}')

#HELP COMMAND FROM HERE -----------------------------------------------------------------------------------------------------


@bot.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "help", description = "Use -Help <command> for extented information on a command. Created by Solace", color = 0x000000)

    em.add_field(name = "Actions", value = "hug, kiss, cuddle, poke, tease, harass, blush, cry, dance, lick, nom, pat, wave, slap, greet, kill")
    em.add_field(name = "Information", value = "Avatar, Stats, serverinfo")
    em.add_field(name = "Music", value = "Join, Summon, leave, volume, play, now_playing, pause, resume, skip, stop, queue, shuffle, remove, loop")
    em.add_field(name = "Fun", value = "rps, toss")

    await ctx.send(embed = em)

#@help.command()
#async def hug(ctx):
#    em = discord.Embed(title = "Hug", description = "To hug a member from the guild.", color = ctx.author.color)
#    em.add_field(name = "**Syntax**", value = "-hug <member>")

#    await ctx.send(embed = em)


#HELP COMMAND ENDS HERE -----------------------------------------------------------------------------------------------------

bot.run('Token')
