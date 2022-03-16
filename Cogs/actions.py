import discord
import random
from discord.ext import commands

class Action(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

#Hugs

    @commands.command()
    async def hug(self, ctx, user: discord.User = None, *, Notes=None):
        hugGifs = ["https://media.giphy.com/media/GMFUrC8E8aWoo/giphy.gif", "https://media.giphy.com/media/wSY4wcrHnB0CA/giphy.gif", "https://media.giphy.com/media/lrr9rHuoJOE0w/giphy.gif", "https://media.giphy.com/media/ZQN9jsRWp1M76/giphy.gif", "https://media.giphy.com/media/fLv2F5rMY2YWk/giphy.gif", "https://media.giphy.com/media/vVA8U5NnXpMXK/giphy.gif", "https://media.giphy.com/media/DjczAlIcyK1Co/giphy.gif", "https://media.giphy.com/media/sUIZWMnfd4Mb6/giphy.gif", "https://c.tenor.com/xIuXbMtA38sAAAAd/toilet-bound-hanakokun.gif","https://c.tenor.com/pcULC09CfkgAAAAC/hug-anime.gif", "https://c.tenor.com/vkiqyZJWJ4wAAAAC/hug-cat.gif", "https://c.tenor.com/rQ2QQQ9Wu_MAAAAC/anime-cute.gif", "https://c.tenor.com/1fXGbo7KvNUAAAAC/hug-anime.gif", "https://c.tenor.com/oQPT1dxDIVQAAAAC/anime-hug.gif", "https://cdn.myanimelist.net/s/common/uploaded_files/1461073447-335af6bf0909c799149e1596b7170475.gif"]

        if not user:
            em = discord.Embed(description=f"{ctx.message.author.mention} hugs", color = 0x000000)
            em.set_image(url=f"{random.choice(hugGifs)}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.message.author.mention} hugs {user.mention}", color = 0x000000)
        embed.set_image(url=f"{random.choice(hugGifs)}")

        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.message.author.mention} hugs {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{random.choice(hugGifs)}")
            await ctx.send(embed=embedZ)

#Kiss

    @commands.command()
    async def kiss(self, ctx, user: discord.User = None, *, Notes=None):
        kissGifs = ["https://media.giphy.com/media/FqBTvSNjNzeZG/giphy.gif", "https://media.giphy.com/media/kU586ictpGb0Q/giphy.gif", "https://media.giphy.com/media/vUrwEOLtBUnJe/giphy.gif", "https://media.giphy.com/media/flmwfIpFVrSKI/giphy.gif", "https://media.giphy.com/media/KmeIYo9IGBoGY/giphy.gif", "https://media.giphy.com/media/bGm9FuBCGg4SY/giphy.gif", "https://c.tenor.com/WijnhV9LiWAAAAAC/anime-kiss.gif", "https://c.tenor.com/oZ04B4Fj8GgAAAAC/anime-kiss.gif", "https://c.tenor.com/dp6A2wF5EKYAAAAC/anime-love.gif", "https://c.tenor.com/8ZcxRredX44AAAAC/kiss-anime.gif", "https://c.tenor.com/Fcc0laaEZ0gAAAAC/lip-lock-kiss.gif", "https://i.pinimg.com/originals/5e/bf/48/5ebf48d780dbcc5c1d4a797aabc577e4.gif", "https://c.tenor.com/693k4pPdrGUAAAAC/anime-kiss.gif"]

        if not user:
            em = discord.Embed(description=f"{ctx.message.author.mention} kisses", color = 0x000000)
            em.set_image(url=f"{random.choice(kissGifs)}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.message.author.mention} kisses {user.mention}", color = 0x000000)
        embed.set_image(url=f"{random.choice(kissGifs)}")

        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.message.author.mention} kisses {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{random.choice(kissGifs)}")
            await ctx.send(embed=embedZ)


#Cuddle

    @commands.command()
    async def cuddle(self, ctx, user: discord.User = None, *, Notes=None):
        CuddleGifs = ["https://i.gifer.com/CzCS.gif", "https://c.tenor.com/WWgamF4xjZcAAAAC/anime-cuddle.gif", "https://i.imgur.com/eTZ063r.gif?noredirect", "http://mrwgifs.com/wp-content/uploads/2013/04/Snuggling-Cuddling-Anime-Girls-Gif-.gif", "https://c.tenor.com/P86Nf3GX1fwAAAAC/anime-cuddle.gif", "https://media0.giphy.com/media/eMpDBxxTzKety/giphy.gif", "https://c.tenor.com/A5ZuMAZ44l8AAAAC/anime-cuddle.gif", "https://i.kym-cdn.com/photos/images/original/000/987/510/f81.gif", "https://pa1.narvii.com/6004/4a589d6cc369ec42110b919cadf579027e7f842b_hq.gif","https://i.pinimg.com/originals/8b/a6/7c/8ba67c2e264576e48daa5a568e1148e6.gif", "https://thumbs.gfycat.com/AshamedAccomplishedCuscus-size_restricted.gif", "https://64.media.tumblr.com/988a4660509af669515a40fd2ee38ada/b6806f9e566d4b2e-1d/s1280x1920/e0827aed786d0eeed23689dc320940b108c4305a.gifv"]

        if not user:
            em = discord.Embed(description=f"{ctx.message.author.mention} cuddles", color = 0x000000)
            em.set_image(url=f"{random.choice(CuddleGifs)}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.message.author.mention} cuddles {user.mention}", color = 0x000000)
        embed.set_image(url=f"{random.choice(CuddleGifs)}")

        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.message.author.mention} cuddles {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{random.choice(CuddleGifs)}")
            await ctx.send(embed=embedZ)


#Poke

    @commands.command()
    async def poke(self, ctx, user: discord.User = None, *, Notes=None):
        PokeGifs = ["https://media.giphy.com/media/pWd3gD577gOqs/giphy.gif", "https://media.giphy.com/media/aZSMD7CpgU4Za/giphy.gif", "https://media4.giphy.com/media/FdinyvXRa8zekBkcdK/giphy.gif", "https://i.gifer.com/SKql.gif", "https://c.tenor.com/nRKOOicoT8YAAAAC/anime-poke.gif", "https://64.media.tumblr.com/tumblr_lkn1twb83X1qbq4v6o1_500.gifv", "https://64.media.tumblr.com/e30fbd6d1358f2a17ecf7d68b6f8129e/tumblr_og1k6m4IdD1qzxv73o1_r1_540.gifv", "https://data.whicdn.com/images/113023956/original.gif", "https://i.makeagif.com/media/1-27-2018/AwAZEo.gif", "https://i.gifer.com/FK0b.gif", "https://media3.giphy.com/media/II5GNcLOhQAuY/giphy.gif", "https://thumbs.gfycat.com/ConcreteChubbyIbizanhound-size_restricted.gif", "https://c.tenor.com/4VxzO9Gg5VYAAAAC/puella-magi-madoka-magica-poke.gif", "https://c.tenor.com/7EkFRiLUn34AAAAC/poke-anime.gif"]

        if not user:
            em = discord.Embed(description=f"{ctx.message.author.mention} pokes", color = 0x000000)
            em.set_image(url=f"{random.choice(pokeGifs)}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.message.author.mention} pokes {user.mention}", color = 0x000000)
        embed.set_image(url=f"{random.choice(PokeGifs)}")

        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.message.author.mention} pokes {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{random.choice(PokeGifs)}")
            await ctx.send(embed=embedZ)


#Tease

    @commands.command()
    async def tease(self, ctx, user: discord.User = None, *, Notes=None):
        teaseGifs = ["https://i.pinimg.com/originals/89/49/1b/89491b19e1cc815a22c16a0203fe859a.gif", "https://c.tenor.com/hkYXjQsuLOcAAAAC/bleh-tongue.gif", "https://i.pinimg.com/originals/f4/26/e1/f426e1f333ebd0d67a7a17c07371cc87.gif", "https://c.tenor.com/xMB5h053L08AAAAC/anime-tease.gif", "https://64.media.tumblr.com/a4046e08081f14b1656cffcfd6544b14/tumblr_p3huk9tY4O1wn2b96o1_540.gifv", "https://64.media.tumblr.com/ff15d5df32484b9054a2cb7b5935b753/06290a213b0d1c3a-8f/s540x810/7f6c24be5561f67202d5a595b7ca3ed37170ae9e.gifv", "https://images-ext-1.discordapp.net/external/81buNdhQx6s8B_ilmCdIwyRh75G9ygubaFXb-259hDM/https/i.imgur.com/QTfCdDv.gif", "https://images-ext-2.discordapp.net/external/bxenUmXlKaMF8zfhrWtxi447LFvDbmwkoNXPvfvHa0o/https/i.imgur.com/uLcZBfN.gif"]

        if not user:
            em = discord.Embed(description=f"{ctx.message.author.mention} is teasing", color = 0x000000)
            em.set_image(url=f"{random.choice(teaseGifs)}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.message.author.mention} is teasing {user.mention}", color = 0x000000)
        embed.set_image(url=f"{random.choice(teaseGifs)}")

        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.message.author.mention} is teasing {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{random.choice(teaseGifs)}")
            await ctx.send(embed=embedZ)

#harass or bully

    @commands.command(aliases=["bully"])
    async def harass(self, ctx, user: discord.User = None, *, Notes=None):
        harassGifs = ["https://c.tenor.com/o2Q0xMRv-4IAAAAd/mahou-shoujo-site-anime.gif", "https://c.tenor.com/JMRAWJgcfF0AAAAC/nagatoro-ijirinaide-nagatoro-san.gif", "https://c.tenor.com/8EF2cz2JB88AAAAd/anime-bully.gif", "https://i.pinimg.com/originals/aa/2e/f7/aa2ef7c6c636dcdc3f0db9ba6c8ae82c.gif", "https://64.media.tumblr.com/c6a8921bbe59e150a0d9f6de589a268b/tumblr_inline_p89j13jUNI1rrn5dn_500.gifv", "https://i.pinimg.com/originals/09/b0/0f/09b00ff69744d42856e9a15132406051.gif", "https://i1.wp.com/pa1.narvii.com/5720/1a163f6b3f19e856d097efe0fd0484ae695ff1cd_hq.gif?resize=500%2C281", "https://c.tenor.com/6614XaRvAoEAAAAC/kuro-usagi-bully.gif"]

        if not user:
            em = discord.Embed(description=f"{ctx.message.author.mention} is harassing", color = 0x000000)
            em.set_image(url=f"{random.choice(harassGifs)}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.message.author.mention} is harassing {user.mention}", color = 0x000000)
        embed.set_image(url=f"{random.choice(harassGifs)}")

        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.message.author.mention} is harassing {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{random.choice(harassGifs)}")
            await ctx.send(embed=embedZ)


#Blush

    @commands.command()
    async def blush(self, ctx, user: discord.User = None, *, Notes=None):
        blushGifs = ["https://media.giphy.com/media/UUjkoeNhnn0K4/giphy.gif", "https://media.giphy.com/media/vIIbrC80HHN7O/giphy.gif", "https://media.giphy.com/media/s5GDgGSuEgVuo/giphy.gif", "https://media.giphy.com/media/QCQxhJALgRF9S/giphy.gif", "https://media.giphy.com/media/6CBGoJnEBbEWs/giphy.gif", "https://media.giphy.com/media/T3Vvyi6SHJtXW/giphy.gif", "https://media.giphy.com/media/FzvuJwrxc6jza/giphy.gif", "https://media.giphy.com/media/UxR7XvbAFqS6Q/giphy.gif", "https://media.giphy.com/media/jxbzLNeT18a3K/giphy.gif", "https://media.giphy.com/media/cxRGi2nJb3cBy/giphy.gif", "https://media.giphy.com/media/4orREzKni7BTi/giphy.gif", "https://media.giphy.com/media/lbk018zqD2jwk/giphy.gif", "https://media.giphy.com/media/l1t5hwEHi77OG1vLlP/giphy.gif", "https://c.tenor.com/JhO1fYhvP14AAAAC/face-blush.gif", "https://c.tenor.com/eBtzvs6BwisAAAAC/anime-girl.gif", "https://c.tenor.com/EclG6PAsZVMAAAAC/blush-anime.gif"]

        if not user:
            em = discord.Embed(description=f"{ctx.message.author.mention} blushes", color = 0x000000)
            em.set_image(url=f"{random.choice(blushGifs)}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.message.author.mention} blushes {user.mention}", color = 0x000000)
        embed.set_image(url=f"{random.choice(blushGifs)}")

        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.message.author.mention} blushes  {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{random.choice(blushGifs)}")
            await ctx.send(embed=embedZ)

#cry

    @commands.command()
    async def cry(self, ctx, user: discord.User = None, *, Notes=None):
        cryGifs = ["https://media.giphy.com/media/ROF8OQvDmxytW/giphy.gif", "https://media.giphy.com/media/shVJpcnY5MZVK/giphy.gif", "https://media.giphy.com/media/N0zizM2fKgGm4/giphy.gif", "https://media.giphy.com/media/L95W4wv8nnb9K/giphy.gif", "https://media.giphy.com/media/11N961lfRaZWfu/giphy.gif", "https://media.giphy.com/media/AI7yqKC5Ov0B2/giphy.gif", "https://media.giphy.com/media/87HkPDUOtN0TC/giphy.gif", "https://media.giphy.com/media/jj8DoqSYVJhPW/giphy.gif", "https://media.giphy.com/media/oAW9QPkQwJqJq/giphy.gif", "https://media.giphy.com/media/b9wQvtFlehup2/giphy.gif", "https://media.giphy.com/media/M4E81QVwE9oBO/giphy.gif", "https://media.giphy.com/media/4iusP4Pbf1L8c/giphy.gif", "https://c.tenor.com/q9V98YHPZX4AAAAC/anime-umaru.gif", "https://c.tenor.com/fBNK66X1CWwAAAAM/cry-anime.gif", "https://c.tenor.com/TtSO-_weHb0AAAAC/aqua-anime.gif", "https://c.tenor.com/2pawKZu4h_oAAAAC/sad-anime.gif", "https://c.tenor.com/ewYhm3sWkEUAAAAd/gray-fullbuster-fairy-tail.gif"]

        if not user:
            em = discord.Embed(description=f"{ctx.message.author.mention} cries", color = 0x000000)
            em.set_image(url=f"{random.choice(cryGifs)}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.message.author.mention} cries {user.mention}", color = 0x000000)
        embed.set_image(url=f"{random.choice(cryGifs)}")

        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.message.author.mention} cries  {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{random.choice(cryGifs)}")
            await ctx.send(embed=embedZ)

#Dance

    @commands.command()
    async def dance(self, ctx, user: discord.User = None, *, Notes=None):
        danceGifs = ["https://media.giphy.com/media/vTqhQldEfAY6c/giphy.gif", "https://media.giphy.com/media/HZboJ5Pkti9k4/giphy.gif", "https://media.giphy.com/media/6k6iDdi5NN8ZO/giphy.gif", "https://media.giphy.com/media/EW3CTnkH6uy3K/giphy.gif", "https://media.giphy.com/media/oTiMS5tKgDSKY/giphy.gif", "https://media.giphy.com/media/J3PFjRm7LB28w/giphy.gif", "https://media.giphy.com/media/3ohzdTADgmPfS1teWk/giphy.gif", "https://c.tenor.com/JJL105F9mSYAAAAC/stripper-pole.gif", "https://c.tenor.com/15NLF1281h8AAAAd/anime-dance.gif", "https://c.tenor.com/EdsiIfnUI6kAAAAC/teeths-dance.gif", ""]

        if not user:
            em = discord.Embed(description=f"{ctx.message.author.mention} dances", color = 0x000000)
            em.set_image(url=f"{random.choice(danceGifs)}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.message.author.mention} dances {user.mention}", color = 0x000000)
        embed.set_image(url=f"{random.choice(danceGifs)}")

        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.message.author.mention} dances {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{random.choice(danceGifs)}")
            await ctx.send(embed=embedZ)

#lick

    @commands.command()
    async def lick(self, ctx, user: discord.User = None, *, Notes=None):
        lickGifs = ["https://media.giphy.com/media/8GiREm7aqMwN2/giphy.gif", "https://media.giphy.com/media/xwsuHAY3oLT68/giphy.gif", "https://c.tenor.com/bgGMTIJhEvEAAAAC/anime-lick-lick.gif", "https://c.tenor.com/5FOgNEcoaYMAAAAC/neck-kisses.gif", "https://c.tenor.com/S5I9g4dPRn4AAAAC/omamori-himari-manga.gif", "https://c.tenor.com/zIU_JbsnMQ8AAAAC/zatch-bell-golden-gash.gif", "https://c.tenor.com/uw6-q_y4xKsAAAAd/%D0%B0%D0%BD%D0%B8%D0%BC%D0%B5-darling-in-the-franxx.gif", "https://c.tenor.com/t6cxb_yox3QAAAAC/lick-ear.gif", "https://c.tenor.com/cuT5hwYqfXgAAAAC/anime-lick.gif", "https://c.tenor.com/Pb1JPfqXpAIAAAAC/lick-licky.gif", "https://c.tenor.com/30jarFTFk5kAAAAC/anime-girl.gif", "https://c.tenor.com/Jel-MDAH0ucAAAAd/anime-zero-two.gif"]

        if not user:
            em = discord.Embed(description=f"{ctx.message.author.mention} licks", color = 0x000000)
            em.set_image(url=f"{random.choice(lickGifs)}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.message.author.mention} licks {user.mention}", color = 0x000000)
        embed.set_image(url=f"{random.choice(lickGifs)}")

        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.message.author.mention} licks {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{random.choice(lickGifs)}")
            await ctx.send(embed=embedZ)

#Nom

    @commands.command()
    async def nom(self, ctx, user: discord.User = None, *, Notes=None):
        nomGifs = ["https://media.giphy.com/media/lay7E1Q6Qoe2jwpTcX/giphy.gif", "https://media.giphy.com/media/CRUMJee9DGjNZaqtaZ/giphy.gif", "https://media.giphy.com/media/qpZ4jZN2cMkgg/giphy.gif", "https://tenor.com/bHBhH.gif", "https://media.giphy.com/media/QEqr30GK4LYmQ/giphy.gif", "https://media.giphy.com/media/HxE2bm0SZWqhW/giphy.gif", "https://tenor.com/7M1l.gif"]

        if not user:
            em = discord.Embed(description=f"{ctx.message.author.mention} noms", color = 0x000000)
            em.set_image(url=f"{random.choice(nomGifs)}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.message.author.mention} noms {user.mention}", color = 0x000000)
        embed.set_image(url=f"{random.choice(nomGifs)}")

        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.message.author.mention} noms {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{random.choice(nomGifs)}")
            await ctx.send(embed=embedZ)

#Pat

    @commands.command()
    async def pat(self, ctx, user: discord.User = None, *, Notes=None):
        patGifs = ["", "", ""]

        if not user:
            em = discord.Embed(description=f"{ctx.message.author.mention} pats", color = 0x000000)
            em.set_image(url=f"{random.choice(patGifs)}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.message.author.mention} pats {user.mention}", color = 0x000000)
        embed.set_image(url=f"{random.choice(patGifs)}")

        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.message.author.mention} pats {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{random.choice(patGifs)}")
            await ctx.send(embed=embedZ)

#Wave

    @commands.command()
    async def wave(self, ctx, user: discord.User = None, *, Notes=None):
        waveGifs = ["", "", ""]

        if not user:
            em = discord.Embed(description=f"{ctx.message.author.mention} waves", color = 0x000000)
            em.set_image(url=f"{random.choice(waveGifs)}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.message.author.mention} waves {user.mention}", color = 0x000000)
        embed.set_image(url=f"{random.choice(waveGifs)}")

        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.message.author.mention} waves {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{random.choice(waveGifs)}")
            await ctx.send(embed=embedZ)

#Slap

    @commands.command()
    async def slap(self, ctx, user: discord.User = None, *, Notes=None):
        slapGifs = ["", "", ""]

        if not user:
            em = discord.Embed(description=f"{ctx.message.author.mention} slaps", color = 0x000000)
            em.set_image(url=f"{random.choice(slapGifs)}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.message.author.mention} slaps {user.mention}", color = 0x000000)
        embed.set_image(url=f"{random.choice(slapGifs)}")

        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.message.author.mention} slaps {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{random.choice(slapGifs)}")
            await ctx.send(embed=embedZ)

#Greet

    @commands.command()
    async def greet(self, ctx, user: discord.User = None, *, Notes=None):
        greetGifs = ["", "", ""]

        if not user:
            em = discord.Embed(description=f"{ctx.message.author.mention} greets", color = 0x000000)
            em.set_image(url=f"{random.choice(greetGifs)}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.message.author.mention} greets {user.mention}", color = 0x000000)
        embed.set_image(url=f"{random.choice(greetGifs)}")

        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.message.author.mention} greets {user.mention}, {Notes}", color = 0x000000)
            embedZ.set_image(url=f"{random.choice(greetGifs)}")
            await ctx.send(embed=embedZ)

#kill

    @commands.command()
    async def kill(self, ctx, user: discord.User = None, *, Notes=None):
        killGifs = ["", "", ""]

        if not user:
            em = discord.Embed(description=f"{ctx.message.author.mention} kills", color = 0x000000)
            em.set_image(url=f"{random.choice(killGifs)}")

            if Notes is None:
                await ctx.send(embed=em)
            return

        embed = discord.Embed(description=f"{ctx.message.author.mention} kills {user.mention}", color= 0x000000)
        embed.set_image(url=f"{random.choice(killGifs)}")

        if Notes is None:
            await ctx.send(embed=embed)
        else:
            embedZ = discord.Embed(description=f"{ctx.message.author.mention} kills {user.mention}, {Notes}", color= 0x000000)
            embedZ.set_image(url=f"{random.choice(killGifs)}")
            await ctx.send(embed=embedZ)


def setup(bot):
    bot.add_cog(Action(bot))
