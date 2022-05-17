import discord
import requests
import time
import json
from discord.ext import commands

TOKEN = 'OTcyOTUwOTE1NzM4ODk4NTUz.GPGz8u.fymqN_cBfCaoLnz4qbHN_SijjC5jym9FKpWIL4'
usersTracking = ['SalvadorShot','Wifies','TheLaSteve']
usersTrackingData = [{},{},{}]
indexTrack = 0

while (indexTrack < len(usersTracking)):
    user = usersTracking[indexTrack]
    mojang_data = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{user}?').json()
    data = requests.get(f"https://api.hypixel.net/player?key=b2182da2-8112-443b-abf3-edb20842f447&uuid={mojang_data['id']}").json()

    usersTrackingData[indexTrack]["username"] = user
    
    # get last login & logout
    try:
        lastLogin = data["player"]["lastLogin"]
        lastLogout = data["player"]["lastLogout"]
        
        usersTrackingData[indexTrack]["lastLogin"] = lastLogin
        usersTrackingData[indexTrack]["lastLogout"] = lastLogout
    except:
        usersTrackingData[indexTrack]["lastLogin"] = 0
        usersTrackingData[indexTrack]["lastLogout"] = 0
    
    
    # total wins
    try:
        totalSoloWins = (data["player"]["stats"]["Bedwars"]["eight_one_wins_bedwars"])
        usersTrackingData[indexTrack]["soloWins"] = totalSoloWins
    except:
        usersTrackingData[indexTrack]["soloWins"] = 0
        
    try:
        totalTwosWins = (data["player"]["stats"]["Bedwars"]["eight_two_wins_bedwars"])
        usersTrackingData[indexTrack]["twosWins"] = totalTwosWins
    except:
        usersTrackingData[indexTrack]["twosWins"] = 0
        
    try:
        totalThreesWins = (data["player"]["stats"]["Bedwars"]["four_three_wins_bedwars"])
        usersTrackingData[indexTrack]["threesWins"] = totalThreesWins
    except:
        usersTrackingData[indexTrack]["threesWins"] = 0
    
    try:
        totalFoursWins = (data["player"]["stats"]["Bedwars"]["four_four_wins_bedwars"])
        usersTrackingData[indexTrack]["foursWins"] = totalFoursWins
    except:
        usersTrackingData[indexTrack]["foursWins"] = 0
    
    
    # total losses
    try:
        totalSoloLoss = (data["player"]["stats"]["Bedwars"]["eight_one_losses_bedwars"])
        usersTrackingData[indexTrack]["soloLoss"] = totalSoloLoss
    except:
        usersTrackingData[indexTrack]["soloLoss"] = 0
        
    try:
        totalTwosLoss = (data["player"]["stats"]["Bedwars"]["eight_two_losses_bedwars"])
        usersTrackingData[indexTrack]["twosLoss"] = totalTwosLoss
    except:
        usersTrackingData[indexTrack]["twosLoss"] = 0
        
    try:
        totalThreesLoss = (data["player"]["stats"]["Bedwars"]["four_three_losses_bedwars"])
        usersTrackingData[indexTrack]["threesLoss"] = totalThreesLoss
    except:
        usersTrackingData[indexTrack]["threesLoss"] = 0
    
    try:
        totalFoursLoss = (data["player"]["stats"]["Bedwars"]["four_four_losses_bedwars"])
        usersTrackingData[indexTrack]["foursLoss"] = totalFoursLoss
    except:
        usersTrackingData[indexTrack]["foursLoss"] = 0

    try:
        recentGames = requests.get(f"https://api.hypixel.net/recentgames?key=b2182da2-8112-443b-abf3-edb20842f447&uuid={mojang_data['id']}").json()
        lastGame = recentGames["games"][0]
        
        usersTrackingData[indexTrack]["game"] = lastGame["gameType"]
        usersTrackingData[indexTrack]["mode"] = lastGame["mode"]
        usersTrackingData[indexTrack]["map"] = lastGame["map"]
    except:
        usersTrackingData[indexTrack]["game"] = "none"
        usersTrackingData[indexTrack]["mode"] = "none"
        usersTrackingData[indexTrack]["map"] = "none"
    indexTrack = indexTrack + 1
    
    time.sleep(0.7)

client = commands.Bot(command_prefix='!')

@client.event
async def on_ready():
    while (True):
        indexCheck = 0
        while (indexCheck < len(usersTrackingData)):
            user = usersTrackingData[indexCheck]["username"]
            mojang_data = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{user}?').json()
            data = requests.get(f"https://api.hypixel.net/player?key=b2182da2-8112-443b-abf3-edb20842f447&uuid={mojang_data['id']}").json()

            try:
                recentGames2 = requests.get(f"https://api.hypixel.net/recentgames?key=b2182da2-8112-443b-abf3-edb20842f447&uuid={mojang_data['id']}").json()
                lastGame2 = recentGames2["games"][0]
                game2 = lastGame2["gameType"]
                mode2 = lastGame2["mode"]
                map2 = lastGame2["map"]
            except:
                game2 = "none"
                mode2 = "none"
                map2 = "none"
            
            # get last login & logout
            try:
                lastLogin2 = data["player"]["lastLogin"]
                lastLogout2 = data["player"]["lastLogout"]
            except:
                lastLogin2 = 0
                lastLogout2 = 0
            
            # check last game
            if (game2 != usersTrackingData[indexCheck]["game"] or mode2 != usersTrackingData[indexCheck]["mode"] or map2 != usersTrackingData[indexCheck]["map"]):
                    response = user + " queued a ", mode2, " game of ",  game2, " on ",  map2
                    await client.wait_until_ready()
                    channel = client.get_channel(974499546086379600)
                    await channel.send(response)
                    usersTrackingData[indexCheck]["game"] = game2
                    usersTrackingData[indexCheck]["mode"] = mode2
                    usersTrackingData[indexCheck]["map"] = map2
            
            # total wins
            try:
                totalSoloWins2 = (data["player"]["stats"]["Bedwars"]["eight_one_wins_bedwars"])
            except:
                totalSoloWins2 = 0
                
            try:
                totalTwosWins2 = (data["player"]["stats"]["Bedwars"]["eight_two_wins_bedwars"])
            except:
                totalTwosWins2 = 0
                
            try:
                totalThreesWins2 = (data["player"]["stats"]["Bedwars"]["four_three_wins_bedwars"])
            except:
                totalThreesWins2 = 0
            
            try:
                totalFoursWins2 = (data["player"]["stats"]["Bedwars"]["four_four_wins_bedwars"])
            except:
                totalFoursWins2 = 0
            
            
            # total losses
            try:
                totalSoloLoss2 = (data["player"]["stats"]["Bedwars"]["eight_one_losses_bedwars"])
            except:
                totalSoloLoss2 = 0
                
            try:
                totalTwosLoss2 = (data["player"]["stats"]["Bedwars"]["eight_two_losses_bedwars"])
            except:
                totalTwosLoss2 = 0
                
            try:
                totalThreesLoss2 = (data["player"]["stats"]["Bedwars"]["four_three_losses_bedwars"])
            except:
                totalThreesLoss2 = 0
            
            try:
                totalFoursLoss2 = (data["player"]["stats"]["Bedwars"]["four_four_losses_bedwars"])
            except:
                totalFoursLoss2 = 0
            
            # check login
            if (usersTrackingData[indexCheck]["lastLogin"] != lastLogin2):
                response = user + " logged on"
                await client.wait_until_ready()
                channel = client.get_channel(974499546086379600)
                await channel.send(response)
                usersTrackingData[indexCheck]["lastLogin"] = lastLogin2
                
            if (usersTrackingData[indexCheck]["lastLogout"] != lastLogout2):
                response =  user + " logged off"
                await client.wait_until_ready()
                channel = client.get_channel(974499546086379600)
                await channel.send(response)
                usersTrackingData[indexCheck]["lastLogout"] = lastLogout2
            
            
            # check results games
            if (usersTrackingData[indexCheck]["soloWins"] != totalSoloWins2):
                response = user + " won Solo Game"
                await client.wait_until_ready()
                channel = client.get_channel(974499546086379600)
                await channel.send(response)
                usersTrackingData[indexCheck]["soloWins"] = totalSoloWins2

            if (usersTrackingData[indexCheck]["twosWins"] != totalTwosWins2):
                response = user + " won Twos Game"
                await client.wait_until_ready()
                channel = client.get_channel(974499546086379600)
                await channel.send(response)
                usersTrackingData[indexCheck]["twosWins"] = totalTwosWins2

            if (usersTrackingData[indexCheck]["threesWins"] != totalThreesWins2):
                response = user + " won Threes Game"
                await client.wait_until_ready()
                channel = client.get_channel(974499546086379600)
                await channel.send(response)
                usersTrackingData[indexCheck]["threesWins"] = totalThreesWins2

            if (usersTrackingData[indexCheck]["foursWins"] != totalFoursWins2):
                response = user + " won Fours Game"
                await client.wait_until_ready()
                channel = client.get_channel(974499546086379600)
                await channel.send(response)
                usersTrackingData[indexCheck]["foursWins"] = totalFoursWins2
            
            if (usersTrackingData[indexCheck]["soloLoss"] != totalSoloLoss2):
                response = user + " lost Solo Game"
                await client.wait_until_ready()
                channel = client.get_channel(974499546086379600)
                await channel.send(response)
                usersTrackingData[indexCheck]["soloLoss"] = totalSoloLoss2

            if (usersTrackingData[indexCheck]["twosLoss"] != totalTwosLoss2):
                response = user + " lost Twos Game"
                await client.wait_until_ready()
                channel = client.get_channel(974499546086379600)
                await channel.send(response)
                usersTrackingData[indexCheck]["twosLoss"] = totalTwosLoss2

            if (usersTrackingData[indexCheck]["threesLoss"] != totalThreesLoss2):
                response = user + " lost Threes Game"
                await client.wait_until_ready()
                channel = client.get_channel(974499546086379600)
                await channel.send(response)
                usersTrackingData[indexCheck]["threesLoss"] = totalThreesLoss2

            if (usersTrackingData[indexCheck]["foursLoss"] != totalFoursLoss2):
                response = user + " lost Fours Game"
                await client.wait_until_ready()
                channel = client.get_channel(974499546086379600)
                await channel.send(response)
                usersTrackingData[indexCheck]["foursLoss"] = totalFoursLoss2

            indexCheck = indexCheck + 1
            time.sleep(0.7)

@client.command(name='track')
async def track(ctx, args):
    mojang_data3 = requests.get(f'https://api.mojang.com/users/profiles/minecraft/{args}?').json()
    data3 = requests.get(f"https://api.hypixel.net/player?key=b2182da2-8112-443b-abf3-edb20842f447&uuid={mojang_data3['id']}").json()
    
    usersTracking.append(args)
    
    usersTrackingData.append({})
    
    usersTrackingData[len(usersTrackingData) - 1]["username"] = args
    
    try:
        lastLogin = data3["player"]["lastLogin"]
        lastLogout = data3["player"]["lastLogout"]
        
        usersTrackingData[len(usersTrackingData) - 1]["username"] = lastLogin
        usersTrackingData[len(usersTrackingData) - 1]["username"] = lastLogout
    except:
        usersTrackingData[len(usersTrackingData) - 1]["username"] = 0
        usersTrackingData[len(usersTrackingData) - 1]["username"] = 0
    
    
    # total wins
    try:
        totalSoloWins = (data3["player"]["stats"]["Bedwars"]["eight_one_wins_bedwars"])
        usersTrackingData[len(usersTrackingData) - 1]["soloWins"] = totalSoloWins
    except:
        usersTrackingData[len(usersTrackingData) - 1]["soloWins"] = 0
        
    try:
        totalTwosWins = (data3["player"]["stats"]["Bedwars"]["eight_two_wins_bedwars"])
        usersTrackingData[len(usersTrackingData) - 1]["twosWins"] = totalTwosWins
    except:
        usersTrackingData[len(usersTrackingData) - 1]["twosWins"] = 0
        
    try:
        totalThreesWins = (data3["player"]["stats"]["Bedwars"]["four_three_wins_bedwars"])
        usersTrackingData[len(usersTrackingData) - 1]["threesWins"] = totalThreesWins
    except:
        usersTrackingData[len(usersTrackingData) - 1]["threesWins"] = 0
    
    try:
        totalFoursWins = (data3["player"]["stats"]["Bedwars"]["four_four_wins_bedwars"])
        usersTrackingData[len(usersTrackingData) - 1]["foursWins"] = totalFoursWins
    except:
        usersTrackingData[len(usersTrackingData) - 1]["foursWins"] = 0
    
    
    # total losses
    try:
        totalSoloLoss = (data3["player"]["stats"]["Bedwars"]["eight_one_losses_bedwars"])
        usersTrackingData[len(usersTrackingData) - 1]["soloLoss"] = totalSoloLoss
    except:
        usersTrackingData[len(usersTrackingData) - 1]["soloLoss"] = 0
        
    try:
        totalTwosLoss = (data3["player"]["stats"]["Bedwars"]["eight_two_losses_bedwars"])
        usersTrackingData[len(usersTrackingData) - 1]["twosLoss"] = totalTwosLoss
    except:
        usersTrackingData[len(usersTrackingData) - 1]["twosLoss"] = 0
        
    try:
        totalThreesLoss = (data3["player"]["stats"]["Bedwars"]["four_three_losses_bedwars"])
        usersTrackingData[len(usersTrackingData) - 1]["threesLoss"] = totalThreesLoss
    except:
        usersTrackingData[len(usersTrackingData) - 1]["threesLoss"] = 0
    
    try:
        totalFoursLoss = (data3["player"]["stats"]["Bedwars"]["four_four_losses_bedwars"])
        usersTrackingData[len(usersTrackingData) - 1]["foursLoss"] = totalFoursLoss
    except:
        usersTrackingData[len(usersTrackingData) - 1]["foursLoss"] = 0

    try:
        recentGames = requests.get(f"https://api.hypixel.net/recentgames?key=b2182da2-8112-443b-abf3-edb20842f447&uuid={mojang_data['id']}").json()
        lastGame = recentGames["games"][0]
        
        usersTrackingData[len(usersTrackingData) - 1]["game"] = lastGame["gameType"]
        usersTrackingData[len(usersTrackingData) - 1]["mode"] = lastGame["mode"]
        usersTrackingData[len(usersTrackingData) - 1]["map"] = lastGame["map"]
    except:
        usersTrackingData[len(usersTrackingData) - 1]["game"] = "none"
        usersTrackingData[len(usersTrackingData) - 1]["mode"] = "none"
        usersTrackingData[len(usersTrackingData) - 1]["map"] = "none"
    
    response = user + " is now being tracked"
    await client.wait_until_ready()
    channel = client.get_channel(974499546086379600)
    await channel.send(response)
    
client.run(TOKEN)