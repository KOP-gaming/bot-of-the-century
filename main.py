import os
import discord
import time
import random
from random import choice

client = discord.Client()

@client.event
async def on_ready():
  print ("we have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("good bot"):
    time.sleep(0.5)
    await message.channel.send("Thank you! :)")
  if message.content.startswith("murnin"):
    await message.channel.send("goodmorning")
  if message.content.startswith("morning"):
    await message.channel.send("goodmorning")
  if message.content.startswith("fuck you"):
    time.sleep(0.5)
    await message.channel.send("fuck you too")
  if message.content.startswith("!c roll D20"):
    rand_num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    rand_num_list = choice(rand_num_list)
    await message.channel.send(rand_num_list)
  if message.content.startswith("!c roll D6"):
    rand_num_list_1 = [1, 2, 3, 4, 5, 6]
    rand_num_list_1 = choice(rand_num_list_1)
    await message.channel.send(rand_num_list_1)
  if message.content.startswith("!c roll D4"):
    rand_num_list_2 = [1, 2, 3, 4]
    rand_num_list_2 = choice(rand_num_list_2)
    await message.channel.send(rand_num_list_2)
  if message.content.startswith("!c roll D12"):
    rand_num_list_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    rand_num_list_3 = choice(rand_num_list_3)
    await message.channel.send(rand_num_list_3)
  if message.content.startswith("!c roll D8"):
    rand_num_list_4 = [1, 2, 3, 4, 5, 6, 7, 8]
    rand_num_list_4 = choice(rand_num_list_4)
    await message.channel.send (rand_num_list_4)


keep_alive.keep_alive()



client.run(os.environ['bot _token'])







#https://codakid.com/guide-to-minecraft-modding-with-java/

#ODUwMzUzMDA0NjI4NDEwMzgw.YLoe8w.2JwilrRheCe6XkVx1TfF-nVDTW4