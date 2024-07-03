import discord
from discord.ext import commands
import random

point = 0

bot = commands.Bot(intents=discord.Intents.all(), command_prefix= "/")
@bot.command('info')
async def command_info(ctx:commands.Context):
    await ctx.send("я демонрстрационный бот")

@bot.command("weather")
async def command_weather(ctx:commands.Context):
    await ctx.send("погода солнечная")

@bot.command("dice")
async def command_dice(ctx:commands.Context):
    global point
    if point > 0:
        point -= 3.5
    dice = random.randint(1,6)
    await ctx.send(dice)
    point += dice

@bot.command("point")
async def command_point(ctx:commands.Context):
    global point
    await ctx.send(point, "- столько у тебя очков")

@bot.command("twenty_one")
async def command_twenty_one(ctx:commands.Context):
    global point
    result = 0
    while result <= 21:
        result += random.randint(0,10)
        await ctx.send(f"Набрано {result}очков продолжить? (y/n)")
        answ = await bot.wait_for("message")
        if answ.content == 'n':
            break
        elif answ.content == 'y':
            continue
        else:
            await ctx.send("такого ответа нет, продолжаем")
            continue
    if result > 21:
        result = 0
    elif result == 21:
        result = 50
    point += result
    await ctx.send(f"В игре 21 очко вы набрали {result} очков")



bot.run('45')
