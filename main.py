import os
import asyncio
import discord
from discord.ext import commands
from decouple import config
from datetime import datetime

bot = commands.Bot(command_prefix=">", intents=discord.Intents.all())

@bot.event 
async def on_ready():
    try:
        synced_commands = await bot.tree.sync()
        print(f"Synced {len(synced_commands)} commands")
    except Exception as e:
        print(f"An error with syncing application commands has occured: {e}")
    
    print(f'Logged on as {bot.user}!')
    
    atividade = discord.Game(name="v1.6 ✅")
    #atividade = discord.Game(name="⚠️ WORKING IN PROGRESS ⚠️")
    await bot.change_presence(status=discord.Status.online, activity=atividade)

    mt_dono = config("user_dono")
    dn = f'{mt_dono}'
        
    now = datetime.now()
    now = now.strftime("%H:%M do dia: %d/%m/%Y")

    cc = bot.get_channel(968277979987869726)
    pingdeploy = round(bot.latency * 1000)
    await cc.send(f'{dn} deploy pronto! Conectado como: {bot.user} com {pingdeploy} de ping às {now}')
    print(f'Deploy pronto! Conectado como: {bot.user} com {pingdeploy} de ping às {now}')
     
@bot.tree.command(name="tst", description="Teste de comando slash")
async def tst(interaction: discord.Interaction):
    await interaction.response.send_message(f"{interaction.user.mention} testado com sucesso") 
    
@bot.tree.command(name="server", description="Mostra as informações do bot no servidor")
async def server(interaction: discord.Interaction):
    latency = round(bot.latency * 1000)
    now1 = datetime.now()
    now1 = now1.strftime("%H:%M do dia %d/%m/%Y")
    await interaction.response.send_message(f"{interaction.user.mention}, o ping do bot no servidor é: {latency} ms na seguinte data: {now1}") 

async def load():
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")
                    
async def main():
    TOKEN = config("secret_token")
    async with bot:
        await load()
        await bot.start(TOKEN)

asyncio.run(main())