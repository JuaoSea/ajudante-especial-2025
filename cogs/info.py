import discord
from discord.ext import commands
from decouple import config

url_link = config("url_link")


class ServerInfo(commands.Cog):
    """Server Info"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def info(self, ctx):
        role_count = len(ctx.guild.roles)

        serverinfo = discord.Embed(title="ServerInfo", timestamp=ctx.message.created_at, color=ctx.author.color)
        serverinfo.set_image(url=f"{url_link}")
        serverinfo.add_field(name="Nome", value=ctx.guild.name, inline=False)
        serverinfo.add_field(name="Membros", value=ctx.guild.member_count, inline=False)
        serverinfo.add_field(name="Nível de verificação", value=f"`{str(ctx.guild.verification_level)}`", inline=False)
        serverinfo.add_field(name="Maior cargo", value=ctx.guild.roles[-1], inline=False)
        serverinfo.add_field(name="Número de cargos", value=str(role_count - 1), inline=False)
        serverinfo.add_field(name="Região", value="`Brazil`", inline=False)

        await ctx.reply(embed=serverinfo)


async def setup(bot):
    await bot.add_cog(ServerInfo(bot))
