import discord
from discord.ext import commands
from decouple import config

user_id = config("user_id")  # ID do usuário autorizado
owner_id = config("owner_id")  # ID do dono do bot

class DropDown(discord.ui.Select):
    def __init__(self, bot):
        options = [
            discord.SelectOption(label='Com certeza ✅', value='1'),
            discord.SelectOption(label='Nem fudendo ❌', value='2'),
            discord.SelectOption(label='Daqui a algumas horinhas 🕑', value='3')
        ]
        super().__init__(placeholder='Aceitas jogar? Responda ⬇️', options=options, min_values=1, max_values=1)
        self.bot = bot  # Aqui estamos passando a instância do bot
        
    async def callback(self, interaction: discord.Interaction):
        self.disabled = True  # Desabilita o menu
        await interaction.message.edit(view=self.view)
        
        res = self.values[0]
        
        if res == '1':
            embed_1 = discord.Embed(
                title="Ready or not noitada",
                description="**Entre na call: [🎮 NOBREZA 🎮](https://discord.gg/qCNz7HSXsK)**",
                colour=788762
            )
            await interaction.response.send_message('Confirmado ✅')  # Primeira resposta obrigatória
            await interaction.followup.send(embed=embed_1)  # Mensagem adicional

            try:
                target2 = await self.bot.fetch_user(owner_id)  # Usando a instância bot
                await target2.send(f'{target2.mention}, {interaction.user.mention} aceitou o convite (Ready or not) ✅')
            except Exception as e:
                print(f"Erro ao enviar mensagem privada: {e}")

        elif res == '2':
            await interaction.response.send_message('Okay, vai tomar no seu cu então porra 👌')
            try:
                target2 = await self.bot.fetch_user(owner_id)  # Usando a instância bot
                await target2.send(f'{target2.mention}, {interaction.user.mention} não aceitou o convite (Ready or not) ❌')
            except Exception as e:
                print(f"Erro ao enviar mensagem privada: {e}")
        elif res == '3':
            embed_2 = discord.Embed(
                title="Ready or not noitada",
                description="**Agilizando o trabalho: [🎮 NOBREZA 🎮](https://discord.gg/qCNz7HSXsK)**",
                colour=788762
            )
            await interaction.response.send_message('Confirmado ✅')  # Primeira resposta obrigatória
            await interaction.followup.send(embed=embed_2)  # Mensagem adicional
            try:
                target2 = await self.bot.fetch_user(owner_id)  # Usando a instância bot
                await target2.send(f'{target2.mention}, {interaction.user.mention} aceitou o convite daqui a algumas horas (Ready or not) 🕑')
            except Exception as e:
                print(f"Erro ao enviar mensagem privada: {e}")

class DropView(discord.ui.View):
    def __init__(self, bot):
        super().__init__()
        self.add_item(DropDown(bot))  # Passando o bot para o DropDown

class Ron(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Transformando para Slash Command
    @discord.app_commands.command(name="ron", description="Convite para uma jogatina de Ready or not")
    async def ron(self, interaction: discord.Interaction, user: discord.User):
        # Verifica se o usuário tem o cargo específico
        role_name = "REI"  # Substitua pelo nome do cargo
        has_role = any(role.name == role_name for role in interaction.user.roles)
        
        if not has_role:
            await interaction.response.send_message("Você não tem permissão para usar este comando.", ephemeral=True)
            return
        
        # 'user' agora é o target que foi passado no comando /ron <ID>
        target = user  # Pegando o usuário que foi especificado no comando
        target2 = await self.bot.fetch_user(owner_id)  # Usando a instância bot
 
        embed_msg = discord.Embed(
            title="Ready or not noitada",
            description=f"*Olá caro {target.mention}! {target2} te chama para uma jogatina de Ready or not, aceitas?*",
            colour=788762
        )
        embed_msg.set_author(name=f"Convite de {target2}")
        embed_msg.set_image(url="https://media1.tenor.com/m/EsNunKSpcgYAAAAd/nvg-ready-or-not.gif")
        embed_msg.set_thumbnail(url="https://cdn2.steamgriddb.com/logo_thumb/781f4a51cef7de9092ef41af4641050a.png")
        
        await interaction.response.send_message(f'{interaction.user.mention}! Convite de noitada enviado com sucesso para {target.mention}')
        await target.send(embed=embed_msg, view=DropView(self.bot))  # Passando o bot para DropView

async def setup(bot):
    await bot.add_cog(Ron(bot))
