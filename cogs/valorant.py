import discord
from discord.ext import commands
from decouple import config

user_id = config("user_id")
owner_id = config("owner_id")


class Valorant(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="valorant")
    @commands.has_permissions(administrator=True)
    async def valorant(self, ctx):
        target = await self.bot.fetch_user(user_id)
        
        embed_msg = discord.Embed(title="Valorant noitada",
                                  description=f"*Olá caro {target.mention}! JuaoSea te chama para uma jogatina de valoras,"
                                              f" aceitas?* \n \n "
                                              f"**Entre na call:  [🎮 NOBREZA 🎮](https://discord.gg/qCNz7HSXsK)**",
                                  colour=16729685)

        embed_msg.set_author(name="Convite de JuaoSea")
        embed_msg.set_image(url="https://c.tenor.com/mXziyAvcV4IAAAAC/sova.gif")
        embed_msg.set_thumbnail(url="https://seeklogo.com/images/V/valorant-logo-FAB2CA0E55-seeklogo.com.png")

        await ctx.reply(f'{ctx.author.mention}! Convite de noitada enviado com sucesso')
        await target.send(embed=embed_msg)
    
async def setup(bot):
    await bot.add_cog(Valorant(bot))