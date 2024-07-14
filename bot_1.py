import discord
from discord.ext import commands
import random
import os
import requests

point = 0
images = os.listdir('images')


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

@bot.command("mem")
async def command_mem(ctx:commands.Context):
    number = random.randint(1,100)
    if number >= 1 and number < 10:
        image_file = images[0]
    elif number > 10 and number < 30:
        image_file = images[1]
    elif number <= 50 and number >= 30:
        image_file = images[2]
    elif number > 50 and number < 60:
        image_file = images[3]
    elif number == 60:
        image_file = images[4]
    elif number > 60 and number < 80:
        image_file = images[5]
    elif number >= 80:
        image_file = images[6]
    
    with open(f'images/{image_file}', 'rb') as file:
        image = discord.File(file)
    await ctx.send('лови мемчик', file = image)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)



bot.run('')
