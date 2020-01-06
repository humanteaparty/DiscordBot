import discord          #imports the discord package where the API wrapper comes from
import random       
import time
from discord.ext import commands

#the commands to control the bot have been assigned to the variable 'client'
client = commands.Bot(command_prefix = '.')


@client.event
#This function will display "genie is ready" in the python shell, when the program is ran. Used to check for bugs.
async def on_ready():
    print("genie is ready")

@client.command()
#This is a simple test function where if I type ".test" in discord the bot should respond with "Test".
async def test(ctx):
    await ctx.send("Test")


@client.event
#fuction (or 'event') is called whenever a message is put in the server which isn't from the bot
async def on_message(message):
    if message.author.id == client.user.id: #what this means is that if the author of the message is the bot, don't respond
        return                              #this makes sure that the bot doesn't reply to itself
    await client.process_commands(message)

    #When I type "rub lamp" into the discord channel, this will bring up this 'if' statement
    wishes = 3
    if "rub lamp" in message.content.lower():
        await message.channel.send(f'I am free! And as you are the one that freed me I will grant you {wishes} wishes!')
        time.sleep(0.5)
        
        wishes = wishes
        while wishes != 0:
            #normal print statements would only print the statement onto the python shell, so I have to use the method 'message.channel.send' to send it do discord
            await message.channel.send("Would you like me to\n[1]Predict your future? \n[2]Summon a priceless gift? \n")
            msg = await client.wait_for('message',check=None , timeout=None)    #wait_for is a function in the documentation which responds to the first event that meets the requirements, in this case the first message the user responds with        
            response_wish = msg.content                                         #response variable now equals the msg variable in the content                                
            answers = ['Yes it will definately happen',
                       'My powers of Precognition are uncertain',
                       'No that will not happen']
        
            
            if response_wish == "future" or response_wish == "1":
                await message.channel.send("What question would you like answered about your future?")
                msg_future = await client.wait_for('message', check=None)   
                await message.channel.send(f'Question: {msg_future.content}\nAnswer: {random.choice(answers)}') #f string used to input variables into string

                wishes = wishes - 1                                                                             #wishes variable will be used to keep the loop going until wishes = 0
                await message.channel.send(f'Wishes left: {wishes}')
                time.sleep(1)

            elif response_wish == "Summon" or response_wish == "2":
                await message.channel.send("What priceless gift should I summon for you?")
                treasure = await client.wait_for('message', check=None)
                await message.channel.send(f':{treasure.content}:')                                             #emojis in discord work by encasing words with colons. E.g. ":smiley:" would display a smiley face 
                wishes = wishes - 1
                await message.channel.send(f'Wishes left: {wishes}')
                await message.channel.send("======================")
                time.sleep(1)

            else:
                                                 #so if the user types something that the bot can't answer to it will loop back
                wishes = wishes
                

        
    
        
        
    if "hi" in message.content.lower():
        await message.channel.send("Hello")

    if "how are you" in message.content.lower():
        await message.channel.send("I am fine. Thank you for asking!")



        

#This allows the code to be connected to my bot
client.run('NjU2NDgyNzUyNTA5NzcxNzc2.XfjV-w.qbC062hVHswqWE7Ppy176B83pbg')
