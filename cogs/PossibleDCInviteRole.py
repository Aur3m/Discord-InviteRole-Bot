import discord
from discord.ext import commands
import time


def find_invite_by_code(invite_list, code):
    for inv in invite_list:
        if inv.code == code:
            return inv
invite_before_join={}

    @commands.Cog.listener()
    async def on_ready(self):
        global invite_before_join
        guild=self.bot.get_guild(PLACE GUILD ID HERE)
        invite_before_join= await guild.invites()

    @commands.Cog.listener()
    async def on_member_join(self, member):
            global invite_before_join
            invites_after_join = await member.guild.invites()
            for invite in invite_before_join:               #Détecte quelle invitation a été utilisée...Puis chaque if regarde si cela correspond à un jeu particulier
                if invite.uses < find_invite_by_code(invites_after_join, invite.code).uses:
                    break
            #print(invite.code)
            if invite.code=="kTxKkVtCn7": #CSGO
                    await member.add_roles(member.guild.get_role(450686675694125057))
            elif invite.code == "XMADCxMTtN":  # BF2042
                    await member.add_roles(member.guild.get_role(858512946542936084))
            elif invite.code == "zr2SqJ2H":  # CSGO Vanity
                    await member.add_roles(member.guild.get_role(450686675694125057))
            elif invite.code=="6xNwDxWWgC": #League Of legends
                    await member.add_roles(member.guild.get_role(483763679893127199))
            elif invite.code=="SuuDrAuCcK": #SW Battlefront2
                    await member.add_roles(member.guild.get_role(800837290468704256))
            elif invite.code=="au4AXFe3C7": #Enlisted
                    await member.add_roles(member.guild.get_role(834532187755249694))
            elif invite.code=="qxMxg3w": #Genshin Impact
                    await member.add_roles(member.guild.get_role(763076544368345129))
            elif invite.code=="tAkxvUA": #Cod Cold War
                    await member.add_roles(member.guild.get_role(765662491983609946))
            elif invite.code=="avA6Cnc": #Rocket League
                    await member.add_roles(member.guild.get_role(483765968229761025))
            elif invite.code=="SQeCKZJ": #Among Us
                    await member.add_roles(member.guild.get_role(755462273342111805))
            elif invite.code=="7grkFmr": #Phasmophobia
                    await member.add_roles(member.guild.get_role(767447959146201108))
            elif invite.code=="CqmfsaAgbf": #Apex Legends
                    await member.add_roles(member.guild.get_role(543151531864621056))
            elif invite.code=="HnKySQp": #Fall Guys
                    await member.add_roles(member.guild.get_role(750396161961230406))
            elif invite.code=="K8GuDrEQRA": #WZ et MW
                    await member.add_roles(member.guild.get_role(629708008917696535)) #Modern Warfare
                    await member.add_roles(member.guild.get_role(687030709356855333)) #Warzone
            elif invite.code=="q8MQKemjvV": #R6
                    await member.add_roles(member.guild.get_role(750392561042194553))
            elif invite.code=="24MFBDH6Vf": #Sea Of Thieves
                    await member.add_roles(member.guild.get_role(750395132846669955))
            elif invite.code=="26beX6SEQk": #Rogue Company
                    await member.add_roles(member.guild.get_role(740146129982717952))
            elif invite.code=="27CqMgDrGm": #Osu!
                    await member.add_roles(member.guild.get_role(787779389974118451))
            elif invite.code=="2CeA7Y45": #Escape From Tarkov
                    await member.add_roles(member.guild.get_role(750395208239153252))
            elif invite.code=="2MtYwgDR": #Valorant
                    await member.add_roles(member.guild.get_role(652585897316843530))
            elif invite.code=="2Rh5jW9Au6": #Minecraft
                    await member.add_roles(member.guild.get_role(775379781217681418))
            elif invite.code=="2cTN6xmC": #Overwatch
                    await member.add_roles(member.guild.get_role(750393514256236655))
            elif invite.code=="2ew943pj": #Outriders
                    await member.add_roles(member.guild.get_role(834478889110994965))
            elif invite.code=="2jkqenF6": #Knockout City
                    await member.add_roles(member.guild.get_role(845942427713404939))








































def setup(bot):
    bot.add_cog(PosDC(bot))