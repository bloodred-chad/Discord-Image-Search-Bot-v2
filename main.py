import discord
from discord.ext import commands
import os
from googleapiclient.discovery import build
from config import api_key, cse_id, token
import random

intents = discord.Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="$", intents=intents)


@client.event
async def on_ready():
    print("!!! Bot Is Online !!!\n")
    await client.tree.sync()


@client.hybrid_command(name="show", with_app_command=True, description="shows a random image from google")
async def show(ctx: commands.Context, *, search: str):
    ran = random.randint(0, 9)
    resource = build("customsearch", "v1", developerKey=api_key).cse()
    result = resource.list(
        q=f"{search}", cx=f"{cse_id}", searchType="image", safe="active"
    ).execute()
    url = result["items"][ran]["link"]
    embed1 = discord.Embed(title=f"Here Your Image ({search}) ")
    embed1.set_image(url=url)
    await ctx.send(embed=embed1)


client.run(token)
