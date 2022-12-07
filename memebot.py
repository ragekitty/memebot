import discord
from discord.ext import commands
import asyncpraw
import asyncio
import random

# Create a new Discord client
intents = discord.Intents().all()
intents.members = True
client = discord.Client(intents=intents)

reddit = asyncpraw.Reddit(
    client_id="reddit id goes here",
    client_secret="reddit secret goes here",
    user_agent="Discord_bot",
    aiohttp_kwargs={"timeout": 10},
)

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    # meme me daddy
    reddit = asyncpraw.Reddit(
        client_id="oid8ZUYxYTA7TmgCWDN1RQ",
        client_secret="cvTuSNwJl3i8-6m1Q9evk2_KLzZBLg",
        user_agent="Discord_bot",
        aiohttp_kwargs={"timeout": 10},
    )
    list = []
    subreddit = await reddit.subreddit("memes")
    async for submission in subreddit.hot(limit=50):
            list.append(submission)
    await message.channel.send(random.choice(list).url)

# Run the bot
client.run('discord key goes here')
