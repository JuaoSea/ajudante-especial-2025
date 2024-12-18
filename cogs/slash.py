import discord
from discord.ext import commands
from datetime import datetime

class Slash(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Criando um comando de barra (slash command)
    @discord.app_commands.command(name="hello", description="Diz 'Olá' para o usuário!")
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"Olá {interaction.user.mention}!")

    @discord.app_commands.command(name="server", description="Mostra as informações do bot no servidor")
    async def server(self, interaction: discord.Interaction):  # Adicionando 'self' aqui
        latency = round(self.bot.latency * 1000)  # Usando 'self.bot.latency'
        now1 = datetime.now()
        now1 = now1.strftime("%H:%M do dia %d/%m/%Y")
        await interaction.response.send_message(f"{interaction.user.mention}, o ping do bot no servidor é: {latency} ms na seguinte data: {now1}") 

async def setup(bot):
    await bot.add_cog(Slash(bot))
