import discord
import os
import sqlite3

client = discord.Client()
conn = sqlite3.connect('grass.db')
c = conn.cursor()

async def send(channel,*args, **kwargs): return await channel.send(*args, **kwargs)

@client.event
async def on_message(message):
    if message.content == "草":
        user_name = message.author.id
        select_sql = 'select * from grass where username='
        username = ('{user_name}').format(user_name=user_name)
        select_sql = select_sql + username
        print(select_sql)
        c.execute(select_sql)
        result=c.fetchone()
        img_name = result[1]
        await message.channel.send(file=discord.File(img_name))

client.run("")