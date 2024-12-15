import discord
import datetime
from datetime import datetime
from discord.ext import commands


class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def bibi(self, ctx):
        await ctx.reply(f"{ctx.author.mention}O Bianchini é um jogador de lol falido")

    @commands.command()
    async def jao(self, ctx):
        await ctx.reply(f'{ctx.author.mention} o dono desse servidor te come em segredo rsrsrs!')

    @commands.command()
    async def hora(self, ctx):

        now1 = datetime.now()
        now1 = now1.strftime("%H:%M do dia: %d/%m/%Y")
        
        await ctx.reply(f"{ctx.author.mention}, a hora certa é: {now1}")

    @commands.command()
    async def convite(self, ctx):
        embed_link = discord.Embed(description=f"{ctx.author.mention} é link que você quer??? Então toma sua safada!",
                                   colour=6606329)

        embed_link.set_author(name="Ajudante Especial")
        embed_link.set_thumbnail(url='https://i.gifer.com/XOsX.gif')
        embed_link.add_field(name="Link:", value='https://discord.gg/TrasB5W', inline=False)

        await ctx.reply(embed=embed_link)


async def setup(bot):
    await bot.add_cog(Commands(bot))
