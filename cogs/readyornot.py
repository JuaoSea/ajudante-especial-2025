import discord
from discord.ext import commands
from decouple import config

user_id = config("user_id")
owner_id = config("owner_id")


class Ron(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ron")
    @commands.has_permissions(administrator=True)
    async def ron(self, ctx):
        target = await self.bot.fetch_user(user_id)

        embed_msg = discord.Embed(title="Ready or not gameplay!!",
                                  description=f"*Olá caro {target.mention}! JuaoSea te chama para uma jogatina de Ready or not,"
                                              f" aceitas?* \n \n "
                                              f"**Entre na call:  [🎮 NOBREZA 🎮](https://discord.gg/e6GV8wk75D)**",
                                  colour=788762)

        embed_msg.set_author(name="Convite de JuaoSea")
        embed_msg.set_image(url="https://media1.tenor.com/m/EsNunKSpcgYAAAAd/nvg-ready-or-not.gif")
        embed_msg.set_thumbnail(url="https://cdn2.steamgriddb.com/logo_thumb/781f4a51cef7de9092ef41af4641050a.png")

        await ctx.reply(f'{ctx.author.mention}! Convite de noitada enviado com sucesso')
        await target.send(embed=embed_msg)
    
async def setup(bot):
    await bot.add_cog(Ron(bot))