import discord
import random
from discord.ext import commands


class Information(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

#Avatar

    @commands.command(aliases=["pfp", "av"])
    async def avatar(self, ctx, member: discord.Member=None):
        if not member:
            member = ctx.author
        embed = discord.Embed(title=f"Avatar Link!", url=str(member.avatar_url), color=discord.Color.teal())
        embed.set_image(url=str(member.avatar_url))
        await ctx.send(embed=embed) ##, mention_author=False


#8ball

    @commands.command(aliases=["8ball", "8b"])
    async def eightball(self, ctx, *, question):
        response = ["It is certain.", "It is decidedly so.", "without a doubt", "Yes, Definitely.",
        "you may rely on it.", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Reply haze, try again",
        "Better not tell you now", "cannot predict now.", "Don't count on it.", "My reply is a no.", "Very doubtful"]
        await ctx.send(f':8ball: Question: {question}\n :8ball: Answer: {random.choice(response)}')

#Stats

    @commands.command()
    async def stats(self,ctx):
        emb = discord.Embed(title="**STATS**",color=0xFF0000)
        emb.add_field(name="Total Servers",value=str(len(self.bot.guilds)),inline=False)
        emb.add_field(name="Latency(s)",value=str(round(self.bot.latency,3)),inline=False)
        emb.add_field(name=f"{ctx.guild} members",value=f'{ctx.guild.member_count}',inline=False)
        await ctx.send(embed=emb)


#ServerStats

    @commands.command(pass_context=True)
    async def serverinfo(self,ctx):
        embed = discord.Embed(
            title = str(ctx.guild.name) + " Server Information",
            color = 0x000000
        )
        embed.set_thumbnail(url=str(ctx.guild.icon_url))
        embed.add_field(name="Owner", value=str(ctx.guild.owner), inline=True)      #FIX OWNER PART
        embed.add_field(name="Server ID", value=str(ctx.guild.id), inline=True)
        embed.add_field(name="Region", value=str(ctx.guild.region), inline=True)
        embed.add_field(name="Member Count", value=str(ctx.guild.member_count), inline=True)
        await ctx.send(embed=embed)



#UserINfo

    @commands.command()
    async def userinfo(self,ctx, member: discord.Member):
        embed = discord.Embed(color=0x000000, timestamp=ctx.message.created_at)

        embed.set_author(name=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"REquested by {ctx.author}", icon_url=ctx.author.avatar_url)

        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Guild name:", value=member.display_name)

        embed.add_field(name="Created at:", value=member.created_at.strftime("%a, %#d, %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a, %#d, %B %Y, %I:%M %p UTC"))




def setup(bot):
    bot.add_cog(Information(bot))
