import discord
from discord.ext import commands
from decouple import config


class Help(commands.Cog):
    """Embeds de ajuda"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def h(self, ctx):
        embed_link = discord.Embed(title="Help", 
                                   description=f"*Já que o burrinho do {ctx.author.mention} não sabe os comandos tá ai uma lista:*",
                                   colour=6606329)

        embed_link.set_author(name="Ajudante Especial")
        embed_link.set_thumbnail(url='https://c.tenor.com/sF5XmjcTrtYAAAAM/patrick-sponge-bob.gif')
        embed_link.add_field(name="Comandos:", value='*>bibi '
                                                     '\n >jao '
                                                     '\n >hora '
                                                     '\n >convite '
                                                     '\n >music '
                                                     '\n >dev '
                                                     '\n >mods'
                                                     '\n >info*', inline=False)

        await ctx.reply(embed=embed_link)

    @commands.command()
    async def music(self, ctx):
        embed_music = discord.Embed(title="Help Music",
                                    description=f"*{ctx.author.mention} tá ai os comandos do bot de música!*",
                                    colour=6606329)

        embed_music .set_author(name="Ajudante Especial")
        embed_music .set_thumbnail(
            url='http://25.media.tumblr.com/dad0a68ec7f3839d635b41bca61540c0/tumblr_mo4jhleyCm1sodyreo1_500.gif')
        embed_music .add_field(name="Comandos:", value="__***/play + [NOME DA MÚSICA]***__ - Adiciona música a fila \n \n "
                                                       "__***/skip***__ - Pula a música atual \n \n"
                                                       "__***/pause***__ - Pausa a reprodução de músicas\n \n"
                                                       "__***/repeat***__ - Repete a ultima música ouvida"
                                                       "__***/list***__ - Mostra a fila de músicas",
                               inline=False)

        await ctx.reply(embed=embed_music)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def dev(self, ctx):
        embed_dev = discord.Embed(title="Help Dev", description=f"*{ctx.author.mention} tá ai os comandos de desenvolvedor do bot*",
                                  colour=6606329)

        embed_dev.set_author(name="Ajudante Especial")
        embed_dev.set_thumbnail(url='https://c.tenor.com/tNGtfhqJWP0AAAAC/haxor.gif')
        embed_dev.add_field(name="Comandos:", value="**>clear + nº de mensagens** "
                                                    "*, por padrão o número definido é:* __*10*__ "
                                                    "\n **>kick + @User + Motivo** "
                                                    "\n **>ban + @User + Motivo ** "
                                                    "\n **>ping**"
                                                    "\n **>server**"
                                                    "\n **>noitada**"
                                                    "\n **>manager**", inline=False)

        await ctx.reply(embed=embed_dev)
        
    @commands.command()
    async def manager(self, ctx):
        LINK1 = config("link1")
        LINK2 = config("link2")
        embed = discord.Embed(title="Manager", 
                                  description=f"*{ctx.atuthor.mention}, tá ai os links de manutenção*", 
                                  colour=7064575)

        embed.set_author(name="Ajudante Especial")
        embed.set_thumbnail(url='https://c.tenor.com/zWnTBUB0_kUAAAAC/michael-scott-the-manager.gif')

        embed.add_field(name="Links:", 
                            value=(f"**Autorizar bot no server:** {LINK1} \n\n **Discord developer portal:** {LINK2}"), 
                            inline=False)

        await ctx.reply(embed=embed)
        
    @commands.command(name="noitada")
    @commands.has_permissions(administrator=True)
    async def noitada(self, ctx):
        nn = ctx.author.mention

        embed_noite = discord.Embed(title="Help Noitada", description=f"*{nn} tá ai os comandos da noitada*",
                                    colour=6606329)

        embed_noite.set_author(name="Ajudante Especial")
        embed_noite.set_thumbnail(url='https://media3.giphy.com/media/3oFzm9LanEHllG3icE/giphy.gif')
        embed_noite.add_field(name="Comandos:", value="**/valorant "
                                                      "\n /mine "
                                                      "\n /ron**",
                              inline=False)

        await ctx.send(embed=embed_noite)
        
    @commands.command(name="manager")
    @commands.has_permissions(administrator=True)
    async def manager(self, ctx):
        LINK1 = config("link1")
        LINK2 = config("link2")

        nn = ctx.author.mention

        embed_man = discord.Embed(title="Manager", description=f"*{nn}, tá ai os links de manutenção*",
                                  colour=7064575)

        embed_man.set_author(name="Ajudante Especial")
        embed_man.set_thumbnail(url='https://c.tenor.com/zWnTBUB0_kUAAAAC/michael-scott-the-manager.gif')
        embed_man.add_field(name="Links:", value="**Autorizar bot no server:** {}"
                                                 "\n"
                                                 "\n **Discord developer portal:** {}".format(LINK1, LINK2),
                            inline=False)

        await ctx.send(embed=embed_man)


async def setup(bot):
    await bot.add_cog(Help(bot))
