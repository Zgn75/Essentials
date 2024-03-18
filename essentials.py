#Essentials API

class es():

    class string():
        
        def before(text: str, kw: str):
            return text[:text.index(kw)]

        def after(text: str, kw: str):
            return text[text.index(kw):].replace(kw,"")
    
    class file():

        def read(file: str):
            try:
                with open(file, "r") as f:
                    return ''.join(f.readlines())

            except:
                return None
        
        def write(file: str, object: str):
            try:
                with open(file, "w") as f:
                    f.write(object)
                    return True
            except:
                return False
        
        def append(file: str, object: str):
            try:
                with open(file, "a") as f:
                    f.write(object)
                    return True

            except:
                return None
            
        def look_for(file: str, object: str):
            try:
                with open(file, "r") as f:
                    list = f.readlines()
                    l_en = []
                    for x in list:
                        l_en.append(x.replace("\n",""))
                    
                    if object in l_en:
                        return True
                    else:
                        return False
                    
            except:
                return None
    
    def exit():
        exit()

    class text():

        def default(text: str):
            return text.capitalize().rstrip()
        
        def title(text: str):

            t: str= ""
            i = 0

            for x in text.split():
                if i == len(text.split()) - 1:
                    t += x.capitalize()
                else:
                    t += x.capitalize() + " "

                i += 1
            
            return t.rstrip()
        
    class templates():

        def discord_py():

            template = """from discord import *
from discord.ext import commands

import discord
import asyncio

intents = discord.Intents().all()
intents.message_content = True
intents.typing = False
intents.presences = False

#Local variables
token = "your-token"
prefix = "your-prefix"

bot = commands.Bot(command_prefix=prefix, intents=intents, help_command=None)

# -------------------------------------------------------------------------

# Definitions

# -------------------------------------------------------------------------

@bot.event
async def on_ready():
    print("Logged in!")

@bot.event
async def on_message(message):
    print("Message detected at {}".format(message.channel.name))

    await bot.process_commands(message)

@bot.command()
async def ping(ctx):
    await ctx.reply("Pong!")

bot.run(token)  # Where 'TOKEN' is your bot token


# bot-invite-link

"""

            if es.file.read("discord.py") == None:
                es.file.write("discord.py", template)
            else:
                loop = True
                i = 2
                while loop:
                    if es.file.read("discord{}.py".format(i)) == None:
                        es.file.write("discord{}.py".format(i), template)
                        loop = False
                    
                    i += 1


# Functions :

"""
es.string.after("Geeks.com", ".") - returns "com"
es.string.before("Geeks.com", ".") - returns "Geeks"
es.file.read("text.txt") - returns text file as a str type
es.file.write("text.txt", "text") - writes/overwrites a text file
es.file.append("text.txt", "text") - appends items to a file
es.file.look_for("text.txt", "item") - looks for item, returns True if found
es.text.default() - Organizes the sentence given --> "hello this is a test " >>> "Hello this is a test"
es.text.title()  - Capitalizes every word in the sentence given --> "hello this is a test " >>> "Hello This Is A Test"
es.templates.discord_py() - Creates a discord py template in the folder that the program was ran
es.exit() - Quits the program
"""