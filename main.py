import discord
from discord.ext import commands
import os
from googleapiclient.discovery import build

#! Import this
import random

client = commands.Bot(command_prefix="$")
api_key = "<YOUR CUSTOM SEARCH API KEY>"
cse_id = "<YOUR PROJECT CSE ID>"
token = "<YOUR DISCORD BOT TOKEN>"


@client.event
async def on_ready():
    print("!!! Bot Is Online !!!\n")
    await bot.tree.sync()


@client.hybrid_command(name="show", with_app_command=True, description="shows a random image from google")
async def show(ctx: commands.Context, search: str):
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
