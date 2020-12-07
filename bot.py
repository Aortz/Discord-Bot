import discord
import os
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv
from discord.ext import commands
import random
import asyncio

#Web Scraping for Quotes
from bs4 import BeautifulSoup
import pandas as pd
import requests

# Connect the path with your '.env' file name
# dotenv_path = join(dirname(__file__), '.env.txt')

# load_dotenv(dotenv_path)
discord_token = os.getenv("DISCORD_TOKEN")
discord_guild = os.getenv("DISCORD_GUILD")


bot = commands.Bot(command_prefix='!')
client  = discord.Client()

@bot.event
async def on_ready():
    print ("Booting up your system")
    print ("I am running on " + bot.user.name)
    print (f'With the ID: {bot.user.id}')

@client.event
async def on_member_join(member):
   await client.get_channel(784995907213066250).send(f"{member.name} has joined")

@client.event
async def on_member_remove(member):
   await client.get_channel(784995907213066250).send(f'Goodbye {member.name}, get lost from my Discord server!')

@bot.event
async def on_member_join1(member):
    await member.create_dm()
    await member.dm_channel.send(
        f"Hi {member.name}, welcome to my Discord server!"
    )
    
hellogreetings = ["hello", "hi", "wassup", "yo", "sup", "@R0bot"]
goodbyegreetings = ["goodbye", "bye", "sayonara", "get lost", "ciao"]

#Responding to User Messages
@bot.event
async def on_message(message):

    if message.content.lower() in hellogreetings:
        await message.channel.send('hey dirtbag')

    if message.content.lower() in goodbyegreetings:
        await message.channel.send('get lost fk face')
    
    if "did u know" in message.content.lower():
        await message.channel.send('know what bitch?')
    
    if 'loli' in message.clean_content.lower():
        await message.add_reaction('🍭') # :lollipop:

    if bot.user.mentioned_in(message) and message.mention_everyone is False:
        if 'help' in message.content.lower():
            await message.channel.send('Try using !help')
        else:
            await message.add_reaction('👀') # :eyes:
            await message.channel.send('hey dirtbag')
        

    if "pek" in message.content.lower():
        await message.channel.send('Send me that 👍 reaction, mate')
        
            
    await bot.process_commands(message)


#Creating Custom Commands
#1. Brooklyn Quotes
URL = 'https://quotecatalog.com/quotes/tv/brooklyn-nine-nine'
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'lxml')
brooklyn_99_quotes = []

for elements in soup.find_all('a', class_="block p-5 font-serif md:text-lg quoteCard__blockquote"):
    brooklyn_99_quotes.append(elements.text.strip())


@bot.command(name="99", help='Responds with a random quote from Brooklyn 99')
async def nine_nine(ctx):
    # URL = 'https://www.yahoo.com/lifestyle/19-brooklyn-nine-nine-quotes-050002008.html?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuZ29vZ2xlLmNvbS8&guce_referrer_sig=AQAAAB4E0GmaTP7Zs2auvemb5fFnCamQKv2tXUrY424iVaLCCljFfLRECNOBrVnq1t6pj6T5kQJ8IqlG7iSMqHMxhVLtQ4G3xAqMOsV3ltvKCekXIa-8VYzox1EKTCkbrMDLE7BsRHvzeGSKo0adHbwCo-iOUki2ZWwn_2tTjubSSo_h'
    # page = requests.get(URL)
    # soup = BeautifulSoup(page.content, 'lxml')
    # brooklyn_99_quotes = []

    # for elements in soup.select('p'):
    #     brooklyn_99_quotes.append(elements.text.strip())

    # response = random.choice(brooklyn_99_quotes[2:13])
    response = random.choice(brooklyn_99_quotes).replace('”', '').replace('“', '')
    await ctx.send(response)

#2. Life Quotes
@bot.command(name="quote", help='Responds with a random quote')

async def life_quotes(ctx):
    URL = 'https://parade.com/937586/parade/life-quotes/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'lxml')
    quotes = []


    for elements in soup.select('p'):
        quotes.append(elements.text.strip())
    life_response = random.choice(quotes)
    await ctx.send(life_response)

#3. Anime Quotes
@bot.command(name="anime", help='Responds with an anime')

async def anime_quotes(ctx):
    URL = 'https://myanimelist.net/topanime.php?type=upcoming'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find(id='content')

    anime_elems = results.find_all('tr', class_='ranking-list')

    quotes = {}

    for anime in anime_elems:
        rank_elems = anime.find('td', class_='rank ac')
        title_elems = anime.find('h3', class_='hoverinfo_trigger fl-l fs14 fw-b anime_ranking_h3')
        if None in (rank_elems, title_elems):
            continue
        quotes[rank_elems.text.strip()] = title_elems.text.strip()


    rank,title = random.choice(list(quotes.items()))
    await ctx.send(f"Rank: {rank} | Title: {title}")

#4. Study Tips
@bot.command(name="studytips", help="Responds with effective study tips")
async def studytips(ctx):
    URL = 'https://www.daniel-wong.com/2019/04/09/study-tips-for-students/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'lxml').find("div", class_="entry-content")
    studyquotes = []


    for elements in soup.select('h3'):
        studyquotes.append(elements.text.strip())      

    response = random.choice(studyquotes)
    await ctx.send(response)

@bot.command(name="studytips2", help="Responds with effective study tips")
async def studytips2(ctx):
    URL = 'https://www.daniel-wong.com/2019/04/09/study-tips-for-students/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'lxml').find("div", class_="entry-content")
    studyquotes = []


    for elements in soup.select('p'):
        studyquotes.append(elements.text.strip())

    response = random.choice(studyquotes)
    await ctx.send(response)




@bot.command(name="breakup", help="Just Suicide")
async def breakup(ctx):
    URL = 'https://everydaypower.com/break-up-quotes/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'lxml')
    buaquotes = []

    for elements in soup.select("p"):
        buaquotes.append(elements.text.strip())
    response = random.choice(buaquotes[11:200]).replace('”', '').replace('“', '')
    await ctx.send(response)

@bot.command(name="pickup", help="Just be Happy")
async def pickup(ctx):
    URL = 'https://parade.com/1039985/marynliles/pick-up-lines/'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'lxml')
    buaquotes = []

    for elements in soup.select("p"):
        buaquotes.append(elements.text.strip())
    response = random.choice(buaquotes[9:109])
    await ctx.send(response)
    

bot.run(discord_token)

