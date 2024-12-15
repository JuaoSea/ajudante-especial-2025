import discord
from discord.ext import commands
from datetime import datetime


class Dev(commands.Cog):
    """Comandos de desenvolvedor"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ping(self, ctx):

        latency = round(self.bot.latency * 1000)
        await ctx.reply(f'Bot ping: {latency} ms')
        
    @commands.command()
    @commands.has_permissions(administrator=True)
    async def server(self, ctx):
        latency = round(self.bot.latency * 1000)
        now1 = datetime.now()
        now1 = now1.strftime("%H:%M do dia %d/%m/%Y")

        await ctx.reply(f"{ctx.author.mention}, o ping do bot no servidor é: {latency} ms na seguinte data: {now1}")

    @commands.command(aliases=['purge'])
    @commands.has_permissions(administrator=True)
    async def clear(self, ctx, amount=20):
        if amount > 101:
            await ctx.send(f'{ctx.author.mention} desculpe, não posso deletar mais que 100 mensagens')
        else:
            await ctx.channel.purge(limit=amount)
            await ctx.send(f'{ctx.author.mention} Feito! 🧹😉')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        print(f"{ctx.author.mention} expulsou o seguinte membro: {member.mention} pelo seguinte motivo: {reason}")
        await ctx.send(f'{ctx.author.mention}, o membro: {member.mention} foi kickado pra casa do baralho 🃏!')

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await member.ban(reason=reason)
        print(f"{ctx.author.mention} baniu o seguinte membro: {member.mention} pelo seguinte motivo: {reason}")
        await ctx.send(f'{ctx.author.mention}, o membro: {member.mention} foi banido pra casa do baralho 🃏!')


async def setup(bot):
    await bot.add_cog(Dev(bot))
