import discord

# id = 735831843169108029

def read_token():
  with open("token.txt", 'r') as f:
    lines = f.readlines()
    return lines[0].strip()

token = read_token()
client = discord.Client()

@client.event
async def on_message(message):
  if message.author == client.user:
        return
  if message.content.find("axie") != -1:
    f = open("scholarship.txt", 'r')
    lines = f.read()
    # print(lines)
    f.close()

  await message.channel.send(lines)
  return

    # await message.channel.send("Name: Alzter G. Aquino")
    # await message.channel.send("21")

client.run(token)