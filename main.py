import json

import discord
import discord_slash

# import asyncio

from discord.ext import commands
from calcs import process_inputs

with open('secrets.json') as fin:
  secrets = json.load(fin)

bot = commands.Bot(command_prefix='!', help_command=None)
@bot.command(name="dinorating")
async def willrating(ctx, name, rating, variant="Rapid"):
  error_msg, prob_success, predicted_date = await process_inputs(name,rating,variant)
  if error_msg == 'No error':
    msg = f"{name} {rating} {variant.title()}: {prob_success} chance within 2 years."
    if int(prob_success[:-1]) > 5: msg += f" If user succeeds, expected date is {predicted_date}."
    await ctx.send(msg)  
  else:
    await ctx.send(error_msg)

slash = discord_slash.SlashCommand(bot, sync_commands=True)
@slash.slash(name="dinorating", description="!dinorating {lichess username} {target rating (must be int less than 3200)} {time control}")
async def _dinorating(ctx, name, rating, variant="Rapid"):
  await dinorating(ctx, name, rating, variant)

bot.run(secrets.get('discord-token'))
