import discord
import random
import asyncio
import aiohttp
import json
from discord import Game
from discord.ext import commands
import time
import datetime
from pytz import timezone
from DiscordAuth import TOKEN
import random
#Trial commit from pi
BOT_PREFIX = ("?", "!")
client = discord.Client()
#client = Bot(command_prefix=BOT_PREFIX)
bot = commands.Bot(command_prefix=BOT_PREFIX,case_insensitive=True)

@bot.event
async def on_ready():
    print("Everything's all ready to go~")
        
@bot.event
async def on_message(message):
    print("The message's content was", message.content)
    if (message.author.bot):
        print("ITS A BOTTTTTTTTTT")
        return
    if "poop" in message.content.lower():
        #emoji = discord.utils.get(bot.get_all_emojis(), name='596882595254501378')
        await message.add_reaction("💩")
    #if "Team Io" in message.guild.name and message.content.startswith("!"):
    #    await message.channel.send("Neil take a nap. Neil will be back. Ping RUdEpernova for help.")
    #   return
    if message.author.name == "ThatCanadianGuy88" and message.channel.name == 'meow-t-of-this-world':
        await message.add_reaction("🤴🏻")
        await message.add_reaction("❤")
        await message.add_reaction("🐱")
    if "weigh in" in message.content.lower() or  "weighin" in message.content.lower() :
        msg = "Remember: NO POOPING or you must fear the wrath of stubbytuna"
        await message.channel.send(msg)
        await  message.add_reaction("🚫")
        await  message.add_reaction("💩")
    #print(type(message.channel))
    if "halo top" in message.content.lower() and "love" in message.content.lower():
        msg = "omg I love halo top."
        await message.channel.send(msg)
    if message.channel.name == 'fitbit-challenges':
     #   print("In FTC pass")
        if "missing invite" in message.content.lower() or \
                "why didn't I get an invite" in message.content.lower() or \
                "no invite" in message.content.lower():
            msg = "Please ensure that you have filled out the pinned google form(use !pin to learn how to see pinned messages) and friended stubbytuna at http://www.fitbit.com/user/752XDX"
            await message.channel.send(msg)
    await bot.process_commands(message)
@bot.command()
async def ping(ctx):
    '''
    Gets the latency of the bot
    '''
    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.channel.send(latency)

@bot.command()
async def links(ctx):
    '''
    Helpful Links
    '''
    msg= "https://www.reddit.com/r/LoseItChallenges/"
    await ctx.channel.send(msg)
@bot.command()
async def pin(ctx):
    '''
    how to view channel pinned messages
    '''
    msg= "On mobile, look for the three dots on the upper right corner to access menu, click on pinned messages.\nOn desktop, click the pin icon in the same line as channel name and description."

    await ctx.channel.send(msg)
@bot.command()
async def description(ctx):
    '''
    How to view channel descriptions
    '''
    msg= "On mobile, look on upper right corner to press the person icon(between search and three dots) to see the description above the member list.\nOn desktop, it should appear in the same line as channel name."
    await ctx.channel.send(msg)
@bot.command()
async def deadline(ctx):
    '''
    Deadline to log weight and activity
    '''
    msg = "The deadline to log weight and activity is Friday 8am EST."
    await ctx.channel.send(msg)


@bot.command(hidden=True)
async def goodbenny(ctx):
    '''
     Good Neil
    '''
    msg = "Thank you! :heart: Glad I can help!"
    await ctx.channel.send(msg)


@bot.command()
async def timeleft(ctx):
    '''
    Hours till logging deadline to help give reference for timezones
    '''

    def days_hours_minutes(td):
        return td.days, td.seconds // 3600, (td.seconds // 60) % 60

    def next_weekday_friday(d, weekday):
        days_ahead = weekday - d.weekday()
        if days_ahead <= 0 and d.hour > 8:  # Target day already happened this week
            days_ahead += 7
        return d + datetime.timedelta(days_ahead)

    eastern = timezone('US/Eastern')
    today = datetime.datetime.now(eastern)
    friday = next_weekday_friday(today,4)
    friday = friday.replace(hour=8, minute=0, second=0, microsecond=0)
    print(today)
    print(friday)
    timediff = friday - today
    timediffsplit = days_hours_minutes(timediff)
    msg = "The deadline to log weight and activity is Friday 8am EST.This is in " + str(timediffsplit[0]) + " days, " + str(timediffsplit[1]) +" hours and " + str(timediffsplit[2]) + " minutes."
    await ctx.channel.send(msg)

@bot.command()
async def echo(ctx, *, content:str):
    '''
    Echos the sentence after
    '''
    if  await chanceOfRickRoll(ctx.channel.name):
        await sendRickRoll(ctx)
        return
    await ctx.channel.send(content)

@bot.command()
async def botoverlord(ctx):
    '''
    Owner info
    '''
    msg = "My bot overload and owner is RUEpernova or RUDEpernova depending on the mood. Feel free to message her with questions and suggestions."
    await ctx.channel.send(msg)

@bot.command()
async def Benny(ctx):
    '''
    Says Hello!
    '''
    msg = "Hello {0.author.mention}".format(ctx)
    await ctx.channel.send(msg)

@bot.command(pass_context = True)
async def ctof(ctx,c_str):
    '''
    Converts C to F. Enter !ctof 28. Do not enter units.
    '''
    try:
        c_value = float(c_str)
    except:
        return
    f_val = int((c_value * 9 /5 + 32)*100)/100
    message = str(c_value) + " deg C is " + str(f_val) + " deg F."
    await ctx.channel.send(message)

@bot.command(pass_context = True)
async def ftoc(ctx,f_str):
    '''
    Converts F to C. Enter !ftoc 98. Do not enter units.
    '''
    try:
        f_value = float(f_str)
    except:
        return
    c_val = int(((f_value- 32)* 5/9)*100)/100
    message = str(f_value) + " deg F is " + str(c_val) + " deg C."
    await ctx.channel.send(message)

@bot.command(pass_context = True)
async def lbstokgs(ctx,lbs_weight_str):
    '''
    Converts lbs to kgs. Enter !lbstokgs Value. ex !lbstokgs 98. Do not enter units.
    '''
    try:
        lbs_weight = float(lbs_weight_str)
    except:
        return
    lbs_weight_rounded = int(lbs_weight*100)/100
    kgs_weight = int(lbs_weight / 2.205 * 100) / 100
    message = str(lbs_weight_rounded) + " lbs is " + str(kgs_weight) + " kgs."
    await ctx.channel.send(message)

@bot.command(pass_context = True)
async def kgstolbs(ctx,kgs_weight_str):
    '''
    Converts kgs to lbs.ex "!kgstolbs 98". Enter !kgstolbs Value. Do not enter units.
    '''
    try:
        kgs_weight = float(kgs_weight_str)
    except:
        return
    kgs_weight_rounded = int(kgs_weight*100)/100
    lbs_weight = int(kgs_weight * 2.205 * 100) / 100
    message = str(kgs_weight_rounded) + " kgs is " + str(lbs_weight) + " lbs."
    await ctx.channel.send(message)

@bot.command(pass_context = True)
async def meterstoft(ctx,meters_str):
    '''
    Converts meters to ft and inches. ex "!meterstoft 1.5". Enter !meterstoft Value. Do not enter units.
    '''
    try:
        meters = float(meters_str)
    except:
        return
    meters_in_ft = meters // .3048
    meters_in_in = int((meters // .3048) % 12)
    message = str(meters) +" meters is " + str(meters_in_ft)+ " feet and"+ str(meters_in_in)+ " inches."
    await ctx.channel.send(message)

@bot.command(pass_context = True)
async def fttometers(ctx,feet_str,inches_str):
    '''
    Converts meters to ft & inc.ex "!meterstoft 5 4". Enter !meterstoft Feet_Value Inches_Value. This means 5ft 4inches Do not enter units.
    '''
    try:
        feet = float(feet_str)
        inches = float(inches_str)
    except:
        return
    meters=  (feet + inches/12)* .3048
    rounded_meters = int(meters*100)/100
    message = str(feet)+ " feet and "+ str(inches)+ " inches is "+str(rounded_meters)+" meters."
    await ctx.channel.send(message)

@bot.command(hidden=True)
async def hype(ctx):
    '''
    GET YOU SOME HYPE!!! (in progress)
    '''
    hypeList = ["HYPE1",
                "HYPE2",
                "HYPE3"
                ]
    print(hypeList)
    msg = hypeList[random.randint(0,len(hypeList)-1)]
    #print(msg)
    await  ctx.channel.send(msg)

@bot.command(hidden=True)
async def bitemythumb(ctx):
    '''
    Can't think of an insult? use this shakepearean insult generator.
    '''
    if await chanceOfRickRoll(ctx.channel.name):
        await sendRickRoll(ctx)
        return
    adjectiveList = ["bootless", "lumpish", "puny", "saucy", "spongy", "viperous", "tottering", "weedy", "lascivious",
                 "fusty", "fishified", "decayed", "languageless", "shallow", "beslubbering", "impertinent", "twangling",
                 "frothy", "mammering", "spleeny", "juggling", "giddy", "wimpled", "pribbling", "bawdy", "wretched",
                 "spleeny", "unmuzzled", "odiferous", "scurvy", "malicious", "execrable", ]
    compoundList = ["wasp-stung", "puppy-headed", "lily-livered", "bat-fowling", "clay-brained", "onion-eyed",
                "cream-faced", "fell-lurking", "swag-bellied", "toad-spotted", "unwash’d", "cony-catching",
                "milk-livered", "lack-brained", "beef-witted", "beetle-headed", "skimble-skamble", "burly-boned",
                "foul-spoken", "malmsey-nosed", "fen-sucked", "long-tongued", "fly-bitten", "boil-brained",
                "nimble-footed", "hare-brained", "guts-griping", "flap-mouthed", "super-serviceable", "marble-hearted",
                "plume-plucked", "folly-fallen", ]
    nounList = ["whoremonger", "bum-baily", "flap-dragon", "hugger-mugger", "malt-worm", "bubble", "shrimp",
            "promise-breaker", "fragment", "barnacle", "boar-pig", "maggot-pie", "ticklebrain", "horse-drench",
            "measle", "nut-hook", "wagtail", "shoulder-clapper", "puttock", "clack-dish", "toad", "time-pleaser", "bug",
            "boil", "fancy-monger", "popinjay", "clotpole", "coxcomb", "drone", "lubber", "whoreson",
            "flibbertigibbet", ]
    authorSentence = "{0.author.name} says ".format(ctx)
    insult = authorSentence+ "Thou "  + adjectiveList[random.randint(0,len(adjectiveList)-1)] + " " + \
             compoundList[random.randint(0, len(compoundList) - 1)] + " " + \
             nounList[random.randint(0, len(nounList) - 1)] +"!"
    await ctx.channel.send(insult)



####################----------GIFS-----------########################
async def chanceOfRickRoll(channelName,authorID=0,percent=3):
    if authorID == 327469084021096457:
        return False
    avoidChannels = ["struggle-shuttle","houston-we-have-problems"]
    if channelName in avoidChannels or "problem" in channelName or "struggle" in channelName:
        return False
    return random.randrange(100) < percent #TIME TO RICK ROLL

async def sendRickRoll(ctx):
    msg = "https://gph.is/1KeL5u6"
    await ctx.channel.send(msg)

@bot.command(hidden=True)
async def rainbows(ctx):
    '''
     rainbows
    '''
    if await chanceOfRickRoll(ctx.channel.name):
        await sendRickRoll(ctx)
        return
    msg = "https://tenor.com/view/rainbow-gif-8764636 "
    await ctx.channel.send(msg)
@bot.command(hidden=True)
async def rooting(ctx):
    '''
    I'm rooting for you patrick
    '''
    if await chanceOfRickRoll(ctx.channel.name):
        await sendRickRoll(ctx)
        return
    msg = "https://tenor.com/view/spongebob-squarepants-patrick-star-im-rooting-for-you-cheer-cheering-gif-5104276"
    await ctx.channel.send(msg)

@bot.command(hidden=True)
async def krostonspecial(ctx):
    '''
     creepy eggplant
    '''
    if await chanceOfRickRoll(ctx.channel.name):
        await sendRickRoll(ctx)
        return
    msg = "https://tenor.com/view/eggplant-faves-happy-gif-12138977"
    await ctx.channel.send(msg)

@bot.command(hidden=True)
async def krostoneggplanet(ctx):
    '''
     creepy eggplant 2
    '''
    if await chanceOfRickRoll(ctx.channel.name):
        await sendRickRoll(ctx)
        return
    msg = "https://tenor.com/view/eggplant-faves-happy-gif-12138977"
    await ctx.channel.send(msg)

@bot.command(hidden=True)
async def spaceelmo(ctx):
    '''
     space elmo
    '''
    if await chanceOfRickRoll(ctx.channel.name):
        await sendRickRoll(ctx)
        return
    msg = "https://tenor.com/view/elmo-dancing-space-gif-13040423"
    await ctx.channel.send(msg)

@bot.command(hidden=True)
async def welcometotheclub(ctx):
    '''
    welcome to the club
    '''
    #msg = "https://gph.is/1KeL5u6"#"https://tenor.com/view/welcome-to-the-club-fist-bump-cool-gif-12226759"
    if await chanceOfRickRoll(ctx.channel.name):
        await sendRickRoll(ctx)
        return
    msg = "https://media.tenor.com/images/1c43814df5a461b7dbaf95682992e25d/tenor.gif"
    await ctx.channel.send(msg)


@bot.command(hidden=True)
async def rueswelcome(ctx):
    '''
    penguinWelcome
    '''
    if await chanceOfRickRoll(ctx.channel.name):
        await sendRickRoll(ctx)
        return
    msg = "https://media.tenor.com/images/78edbb1f8c34b17b20e9e0987914001e/tenor.gif"
    await ctx.channel.send(msg)

#@bot.command(hidden=True)
#async def stabbystab(ctx):
#    '''
#    BEST GIF EVER
#    '''
#    await ctx.message.channel.send('', file=discord.File('stabbystab.gif', 'stabbystab.gif'))
@bot.command(hidden=True)
async def stabbystab(ctx):
    '''
    BEST GIF  from imgur
    '''
    if await chanceOfRickRoll(ctx.channel.name):
        await sendRickRoll(ctx)
        return
    msg = "https://imgur.com/0HW9DAD"
    await ctx.channel.send(msg)

@bot.command(hidden=True)
async def whalehello(ctx):
    '''
    Whale hello there gif
    '''
    if await chanceOfRickRoll(ctx.channel.name):
        await sendRickRoll(ctx)
        return
    msg = "https://tenor.com/view/whale-hellothere-hello-hi-hey-gif-4505186"
    await ctx.channel.send(msg)


@bot.command(hidden=True)
async def titleofyoursextape(ctx):
    '''
    Title of your sex tape
    '''
    if await chanceOfRickRoll(ctx.channel.name):
        await sendRickRoll(ctx)
        return
    msg = "https://tenor.com/view/title-of-your-sex-tape-jake-peralta-brooklyn-nine-nine-andy-samberg-nbc-gif-13615436"
    await ctx.channel.send(msg)

@bot.command(hidden=True)
async def rickroll(ctx):
    '''
    RICK IS HERE!
    '''
    msg = "https://gph.is/1KeL5u6"
    await ctx.channel.send(msg)


@bot.command(hidden=True)
async def hydration(ctx):
    '''
     DRINK WATER
    '''
    msg = "https://imgur.com/gallery/ByENJvZ"
    await ctx.channel.send(msg)
###########################################################
######################---PETS----##################################
@bot.command(pass_context=True)
async def belle(ctx, loss):
    '''
    How many belle(lxgo's cat) have you lost?
    '''
    petname = 'Belle'
    petweight = 10.8
    petpiclink = 'https://imgur.com/7g5mM9W'
    loss = int(loss)
    petloss = int(loss / petweight * 100) / 100
    message = 'You have to hold '+ str(petloss) +" "+ petname+ "'s to weigh the same now. She is also working on weight loss so she can be your buddy! Enjoy the cuddles and keep rocking it!"
    await ctx.channel.send(message)
    await ctx.channel.send(petpiclink)

@bot.command(pass_context=True)
async def pickle(ctx, loss):
    '''
    How many pickles(Kr0st0n's cat) have you lost?
    '''
    petname = 'Pickle'
    petweight = 8
    petpiclink = 'https://imgur.com/ytV0vSw'
    loss = int(loss)
    petloss = int(loss / petweight * 100) / 100
    message = 'You have to hold '+ str(petloss) +" "+ petname+ "'s to weigh the same now. Enjoy the cuddles and keep rocking it!"
    await ctx.channel.send(message)
    await ctx.channel.send(petpiclink)

@bot.command(pass_context=True)
async def wuffles(ctx, loss):
    '''
    How many wuffles(Vicarious Astrodots's pup) have you lost?
    '''
    petname = 'Wuffles'
    petweight = 9.7
    petpiclink = 'https://imgur.com/pc1T9F7'
    loss = int(loss)
    petloss = int(loss / petweight * 100) / 100
    message = 'You have to hold '+ str(petloss) +" "+ petname+ "'s to weigh the same now. Enjoy the cuddles and keep rocking it!"
    await ctx.channel.send(message)
    await ctx.channel.send(petpiclink)

@bot.command(pass_context=True)
async def Laika(ctx, loss):
    '''
    Laika is the first dog in space!
    '''
    petname = 'Laika'
    petweight = 11
    petpiclink = 'https://imgur.com/vB0hPDW'
    loss = int(loss)
    petloss = int(loss / petweight * 100) / 100
    message = 'You have to hold '+ str(petloss) +" "+ petname+ "'s to weigh the same now. Enjoy the cuddles and keep rocking it!"
    await ctx.channel.send(message)
    await ctx.channel.send(petpiclink)

@bot.command(pass_context=True)
async def logan(ctx, loss):
    '''
    How many logans(jenrazzle's puppy) have you lost?
    '''
    petname = 'Logan'
    petweight = 35
    petpiclink = 'https://imgur.com/cQxPKpK'
    loss = int(loss)
    petloss = int(loss / petweight * 100) / 100
    message = 'You have to hold '+ str(petloss) +" "+ petname+ "'s to weigh the same now.Enjoy the cuddles and keep rocking it!"
    await ctx.channel.send(message)
    await ctx.channel.send(petpiclink)


@bot.command(pass_context=True)
async def daisy(ctx, loss):
    '''
    How many daisy(Majestic Space Poet's dog) have you lost?
    '''
    petname = 'Daisy'
    petweight = 66
    petpiclink = 'https://imgur.com/Ha15uJd'
    loss = int(loss)
    petloss = int(loss / petweight * 100) / 100
    message = 'You have to hold '+ str(petloss) +" "+ petname+ "'s to weigh the same now. Daisy is proud of you!"
    await ctx.channel.send(message)
    await ctx.channel.send(petpiclink)

@bot.command(pass_context=True)
async def gatsby(ctx, loss):
    '''
    How many gatsby(grumpyspacething's cat) have you lost?
    '''
    petname = 'Gatsby'
    petweight = 16
    petpiclink = 'https://imgur.com/vGjA1ok'
    loss = int(loss)
    petloss = int(loss / petweight * 100) / 100
    message = 'You have to hold '+ str(petloss) +" "+ petname+ "'s to weigh the same now! Gatsby knows saying no to unhealthy food is hard. Gatsby is proud of your willpower! Now where did his tuna go?!"
    await ctx.channel.send(message)
    await ctx.channel.send(petpiclink)

@bot.command(pass_context=True)
async def Matilda(ctx, loss):
    '''
    How many Matilda(grumpyspacething's cat) have you lost?
    '''
    petname = 'Matilda'
    petweight = 10
    petpiclink = "https://imgur.com/wTdADdx"
    loss = int(loss)
    petloss = int(loss / petweight * 100) / 100
    message = 'You have to hold '+ str(petloss) +" "+ petname+ "'s to weigh the same now! Matilda wants to be your exercise buddy! She’s so helpful! You’re her favorite!"
    await ctx.channel.send(message)
    await ctx.channel.send(petpiclink)

@bot.command(pass_context=True)
async def emily(ctx, loss):
    '''
    How many emily(stubbytuna's pup) have you lost?
    '''
    petname = 'Emily'
    petweight = 52
    petpiclink = "https://imgur.com/JjjBv6t"
    loss = int(loss)
    petloss = int(loss / petweight * 100) / 100
    message = 'You have to hold '+ str(petloss) +" "+ petname+ "'s to weigh the same now! Enjoy the cuddles!"
    await ctx.channel.send(message)
    await ctx.channel.send(petpiclink)

@bot.command(pass_context=True)
async def marley(ctx, loss):
    '''
    How many Marleys(Wymaness's pup) have you lost?
    '''
    petname = 'Marley'
    petweight = 125
    petpiclink = "https://imgur.com/ztMlTur"
    loss = int(loss)
    petloss = int(loss / petweight * 100) / 100
    message = 'You have to hold '+ str(petloss) +" "+ petname+ "'s to weigh the same now! Marley is a big floofler. Marley is impressed with you!"
    await ctx.channel.send(message)
    await ctx.channel.send(petpiclink)

######################---CHALLENGE BASED----##################################
@bot.command()
async def timeline(ctx):
    '''
    Shows a timeline for the challenge
    '''
    msg = '''September 27th - Signups open\n
October 4th - Week 0, Establish challenge goals, signups open through end of week\n
October 11th - Week 1, Head to Head battles begin, Signups are closed\n
October 18th - Week 2\n
October 25th - Week 3\n
November 1st- Week 4\n
November 8th - Week 5\n
November 15th - Week 6\n
November 22nd - Week 7, Last Head to Head Battle\n
November 29th - Results and next challenge announcement'''
    await ctx.channel.send(msg)

@bot.command()
async def iofacts(ctx):
    '''
    Gets all the iofacts. More efficient, more lame than iofact
    '''
    factList = ["Jupiter-bae: Io is the innermost of the four Galilean moons of the planet Jupiter.",
               "BOOM. Io is the most volcanically active world in the solar system. Io even has lakes of molten silicate lava on its surface.",
                "Io is slightly larger than earth's moon. #weirdflexbutokay",
               "Get my good side: Over 1.8 Earth days, Io rotates once on its axis and completes one orbit of Jupiter, causing the same side of Io to always face Jupiter.",
               "Io’s very thin atmosphere is primarily sulfur dioxide, an important compound used in winemaking since Roman times. ",
               "Io’s volcanoes are at times so powerful that they are seen with large telescopes on Earth. :eyes:",
               "Io is the best team within the loseit challenge. Yes, this is a fact.",
               "My Bot Lord hasn't had time to update to Halloween facts. Sincerest Apologies for the lack of effot from her. I deal with this everyday. Save me plz."]
    await  ctx.channel.send("\n".join(factList))

numTried = 0
while numTried<10:
	try:
		bot.run(TOKEN)
		numTried = 0
	except:
		time.sleep(30)
		numTried =numTried + 1