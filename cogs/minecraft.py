import discord
from discord.ext import commands
from decouple import config

user_id = config("user_id")
owner_id = config("owner_id")


class Minecraft(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="mine")
    @commands.has_permissions(administrator=True)
    async def mine(self, ctx):
        target = await self.bot.fetch_user(user_id)

        embed_msg = discord.Embed(title="Minecraft gameplay",
                                  description=f"*Olá caro {target.mention}! JuaoSea te chama para uma jogatina de minezin,"
                                              f" aceitas?* \n \n "
                                              f"**Entre na call:  [🎮 NOBREZA 🎮](https://discord.gg/e6GV8wk75D)**",
                                  colour=7448644)

        embed_msg.set_author(name="Convite de JuaoSea")
        embed_msg.set_image(url="https://c.tenor.com/j0KEi6tfpRcAAAAC/minecraft-boxer.gif")
        embed_msg.set_thumbnail(url="https://cdn.icon-icons.com/icons2/2699/PNG/512/minecraft_logo_icon_168974.png")

        await ctx.reply(f'{ctx.author.mention}! Convite de noitada enviado com sucesso')
        await target.send(embed=embed_msg)
    
async def setup(bot):
    await bot.add_cog(Minecraft(bot))