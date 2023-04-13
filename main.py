#MTA5MzQwNDUyNDEwODA2Mjc2Mg.GUa2HO.ELcIXwgPB5LeSsFkavr8DjwxHF3_pvaN-eOeWk
import discord

# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной client и передаем все привелегии
client = discord.Client(intents = intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    elif message.content.startswith('как дела'):
        await message.channel.send("норм")
    elif message.content.startswith('го в бс'):
        await message.channel.send("я не могу, я же бот")
    elif message.content.startswith('скинь мем'):
        await message.channel.send("«Иду себе иду, никого не трогаю...» - так начинается каждый рассказ безрукого мальчика.")
    else:
        await message.channel.send(message.content)

client.run("MTA5MzQwOTQxNzgxNjQ0OTEzNg.G10lZ-.ZcWZ_IIW63Z_xswa3GBHLWkfRsD0cSN_1a9c9E")
















