from discord.ext import commands


class Error(commands.Cog):
    """Comandos de interação"""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.reply(f"O comando '{ctx.message.content}' não existe, tente novamente!")

        if isinstance(error, commands.MissingPermissions):
            await ctx.reply(f"Você não tem permissão para usar esse comando {ctx.author.name}! ⚠️")

        if isinstance(error, commands.MissingAnyRole):
            nobreza_id = '<@&759856227626385418>'
            await ctx.reply(f"Você não é da {nobreza_id} {ctx.author.name}! ⚠️")


async def setup(bot):
    await bot.add_cog(Error(bot))