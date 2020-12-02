import os
import random
import asyncio

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='roll_dice', help='Simulates rolling dice.')
async def roll_dice(ctx, number_of_dice=1, number_of_sides=6):
    dice = [
        str(random.choice(range(1, number_of_sides + 1)))
        for _ in range(number_of_dice)
    ]
    await ctx.send(', '.join(dice))

@bot.command(name='roll', help='Roll random number.')
async def roll(ctx, range_left=0, range_right=101):
    roll_number = str(random.choice(range(range_left, range_right)))
    await ctx.send(roll_number)

@bot.command(name='votekick', help='Poll to kick someone')
async def votekick(ctx, target:str):
    await ctx.send(f'Vote for kicking {target} has started. You have 120 seconds to vote')
    async def votesleep(ctx):
        asyncio.sleep(120)
        await ctx.send(f'Vote has ended. The majority has voted for')
    async def print_print(ctx):
        await print("HELLO")


bot.run(TOKEN)