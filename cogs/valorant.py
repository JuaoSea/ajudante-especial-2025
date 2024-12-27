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
        super().__init__(
            placeholder='Aceitas jogar? Responda ⬇️', 
            options=options, 
            min_values=1, 
            max_values=1
        )
        self.bot = bot

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.defer()  # Previne timeout de 3 segundos

        res = self.values[0]
        try:
            target2 = await self.bot.fetch_user(owner_id)

            if res == '1':
                embed_1 = discord.Embed(
                    title="Valorant noitada",
                    description="**Entre na call: [🎮 NOBREZA 🎮](https://discord.gg/qCNz7HSXsK)**",
                    colour=discord.Colour.orange()
                )
                await interaction.followup.send('Confirmado ✅', embed=embed_1)
                await target2.send(f"{interaction.user.mention} aceitou o convite (Valorant) ✅")

            elif res == '2':
                await interaction.followup.send("Okay, vai tomar no seu cu então porra 👌")
                await target2.send(f"{interaction.user.mention} recusou o convite (Valorant) ❌")

            elif res == '3':
                embed_2 = discord.Embed(
                    title="Valorant noitada",
                    description="**Agilizando o trabalho: [🎮 NOBREZA 🎮](https://discord.gg/qCNz7HSXsK)**",
                    colour=discord.Colour.orange()
                )
                await interaction.followup.send('Confirmado ✅', embed=embed_2)
                await target2.send(f"{interaction.user.mention} aceitou o convite daqui a algumas horas (Valorant) 🕑")

        except discord.Forbidden:
            print("Não foi possível enviar a DM. Verifique se o usuário permite mensagens privadas.")
        except Exception as e:
            print(f"Erro desconhecido: {e}")

class DropView(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.add_item(DropDown(bot))

class Valorant(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="valorant", description="Convite para uma jogatina de Valorant")
    async def valorant(self, interaction: discord.Interaction, user: discord.User):
        # Verifica se o usuário tem o cargo específico
        role_name = "REI"  # Substitua pelo nome do cargo correto
        has_role = any(role.name == role_name for role in interaction.user.roles)

        if not has_role:
            await interaction.response.send_message(
                "Você não tem permissão para usar este comando.", ephemeral=True
            )
            return

        # O 'user' agora é o usuário especificado no comando
        target = user
        target2 = await self.bot.fetch_user(owner_id)

        embed_msg = discord.Embed(
            title="Valorant noitada",
            description=f"*Olá caro {target.mention}! {target2.mention} te chama para uma jogatina de Valorant, aceitas?*",
            colour=discord.Colour.orange()
        )
        embed_msg.set_author(name=f"Convite de {target2}")
        embed_msg.set_image(url="https://c.tenor.com/mXziyAvcV4IAAAAC/sova.gif")
        embed_msg.set_thumbnail(url="https://seeklogo.com/images/V/valorant-logo-FAB2CA0E55-seeklogo.com.png")

        await interaction.response.send_message(
            f"{interaction.user.mention}! Convite de noitada enviado com sucesso para {target.mention}.", ephemeral=True
        )

        try:
            await target.send(embed=embed_msg, view=DropView(self.bot))
        except discord.Forbidden:
            await interaction.followup.send(
                f"Não foi possível enviar mensagem privada para {target.mention}.", ephemeral=True
            )
        except Exception as e:
            print(f"Erro desconhecido ao enviar DM: {e}")

async def setup(bot):
    await bot.add_cog(Valorant(bot))
