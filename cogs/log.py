import datetime
from datetime import datetime
from discord.ext import commands


class Register(commands.Cog):
    """Registro do bot de música"""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if "/play" in message.content:
            canal = self.bot.get_channel(968277979987869726)
            
            now2 = datetime.now()
            now2 = now2.strftime("%H:%M do dia: %d/%m/%Y")

            await canal.send(f'User: {message.author.name}, utilizou o bot de música às: {now2}')


async def setup(bot):
    await bot.add_cog(Register(bot))
