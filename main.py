import discord
import os
from discord.ext import commands
import time
from dotenv import load_dotenv
intents = discord.Intents.all()
intents.typing = True
intents.presences = True
bot = commands.Bot(command_prefix='!', intents=intents)
load_dotenv()
token =os.getenv("token")
@bot.event
async def on_ready():
  print(f'Logged in as {bot.user.name} ({bot.user.id})')
  # Role emojis and corresponding roles
role_emojis = {
    '🚀': 'Code Astronauts',
    '🔮': 'Digital Wizards',
    '💡': 'Luminary UI/UX',
    '🦄': 'Design Unicorns',
    '🔌': 'Plugin Pirates',
    '💻': 'Terminal Titans',
    '🌐': 'Cybernetic Explorers'
} 
MESSAGE_ID = 1128994539240169512
CHANNEL_ID = 1128618287681523722
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    # Fetch the message
    channel = bot.get_channel(CHANNEL_ID)
    message = await channel.fetch_message(MESSAGE_ID)
    # Add reactions
    for emoji in role_emojis.keys():
        await message.add_reaction(emoji)
@bot.event
async def on_raw_reaction_add(payload):
    # Make sure the reaction is for the right message
    if payload.message_id != MESSAGE_ID:
        return

    guild = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    emoji = str(payload.emoji)

    if emoji in role_emojis.keys():
        role_name = role_emojis[emoji]
        role = discord.utils.get(member.guild.roles, name=role_name)

        if role:
            await member.add_roles(role)
            print(f"Added role {role} to user {member}")
        else:
            print(f"Role {role_name} not found")
@bot.event
async def on_raw_reaction_remove(payload):
    # Make sure the reaction is for the right message
    if payload.message_id != MESSAGE_ID:
        return

    guild = bot.get_guild(payload.guild_id)
    member = guild.get_member(payload.user_id)
    emoji = str(payload.emoji)

    if emoji in role_emojis.keys():
        role_name = role_emojis[emoji]
        role = discord.utils.get(member.guild.roles, name=role_name)

        if role:
            await member.remove_roles(role)
            print(f"Removed role {role} from user {member}")
        else:
            print(f"Role {role_name} not found")
#welcome message
@bot.event
async def on_member_join(member):
    # Find a channel by its name
    channel = discord.utils.get(member.guild.channels, name='welcome')
    if channel:
        await channel.send(f'Welcome to the server, @{member.mention}) !')
#personality test
@bot.command()
async def start(ctx):
    # List of questions
    questions = ["🌞Early bird(1) or 🦉night owl(2)?",
                 "🐱Cats(1) or 🐶dogs(2)?",
                 "🏙️City(1) or 🌾countryside(2)?",
                 "🎲Spontaneous(1) or 📅planned(2)?",
                 "🚪Introvert(1) or 🌍extrovert(2)?",
                 "🍰Sweet(1) or 🍟savory(2)?",
                 "😊Optimist(1) or 😔pessimist(2)?",
                 "🎨Arts(1) or 🔬sciences(2)?",
                 "🏕️Adventure(1) or 🏖️relaxation(2)?",
                 "🦸‍♂️Leader(1) or 👥follower(2)?",
                 "❤️Do you believe in love at first sight? Yes(1) or No(2)",
                 "🧑‍💻Do you prefer working alone(1) or in a 🤝team(2)?", "What is your gender (1) male (2) female?"]
                
    options = ["1⃣", "2⃣"] 
   # Personality types
    personalities = {
        "The Ambitious Dreamer": [1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 1, 1 , {'male': 'https://media.discordapp.net/attachments/1128269667673309214/1128270245648408606/mdjourneyuser_Generate_a_vivid_and_detailed_description_of_a_vi_c587c036-10cd-4f05-8fed-734a0a8a30d4.png', 'female': 'https://media.discordapp.net/attachments/1128269667673309214/1128270496778174464/mdjourneyuser_Generate_a_vivid_and_detailed_description_of_a_vi_716ec53e-6927-4c10-9ce3-2c1ed7d367cb.png'}],
        "The Free-Spirited Realist": [2, 2, 2, 1, 2, 2, 2, 2, 1, 2, 2, 2,{'male': 'https://media.discordapp.net/attachments/1128269667673309214/1128270973196574762/mdjourneyuser__Create_the_persona_of_a_captivating_man_with_the_d837ea89-4d29-40cb-ac1b-a7d968ad7f98.png', 'female': 'https://media.discordapp.net/attachments/1128269667673309214/1128270646854570054/mdjourneyuser__Create_the_persona_of_a_captivating_woman_with_t_970c9c91-2762-43fc-8cd3-e689ff9070ce.png'}],
        "The Artistic Adventurer": [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, {'male': 'https://media.discordapp.net/attachments/1128269667673309214/1128271666024284160/mdjourneyuser_Create_a_4K_resolution_image_of_a_photogenic_man__abb24786-33d1-4776-bbec-73a33c1dbf4c.png', 'female': 'https://media.discordapp.net/attachments/1118443750415413268/1129040599186686123/mdjourneyuser_A_photorealistic_8K_Octane_render_of_a_distinctiv_27183929-589b-470d-a300-4c36bffbefd5.png?width=413&height=413'}],
        "The Intellectual Introvert": [2, 1, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1,{'male': 'https://media.discordapp.net/attachments/1128269667673309214/1128271665713913956/mdjourneyuser_Create_a_4K_resolution_image_capturing_a_photogen_e96a328a-9957-44e1-b94c-cbeb09eb11e8.png', 'female': 'https://media.discordapp.net/attachments/1118443750415413268/1129041432058024046/mdjourneyuser_A_high-resolution_photorealistic_image_of_a_woman_4423994f-ccbf-488d-8cfe-fc1d50a1be81.png?width=413&height=413'}],
        "The Dynamic Leader": [1, 2, 1, 2, 2, 1, 1, 2, 1, 1, 2, 2,{'male': 'https://media.discordapp.net/ephemeral-attachments/1118443750415413268/1129042448434352219/mdjourneyuser_A_high-quality_8K_image_of_a_handsome_manMAKE_SUR_8325fb26-0cb7-47e3-9575-282149bdc633.png?width=413&height=413', 'female': 'https://media.discordapp.net/attachments/1118443750415413268/1129043196840771655/mdjourneyuser_A_stunning_8K_image_of_a_beautiful_woman_make_sur_681e37e7-ea0d-44b7-9522-979e6c7134e3.png?width=413&height=413'}],
        "The Relaxed Optimist": [2, 1, 2, 1, 2, 2, 1, 1, 2, 2, 1, 1,{'male': 'https://media.discordapp.net/attachments/1118443750415413268/1129044910641795203/mdjourneyuser_An_8K_image_of_a_charismatic_man_make_sure_men_fa_2737a790-706e-4327-92e8-0203cf0d37b2.png?width=413&height=413', 'female': 'https://media.discordapp.net/attachments/1128269667673309214/1128270379295719537/mdjourneyuser_Generate_a_vivid_and_detailed_description_of_a_be_130532c1-a1b3-4cc5-9ead-5958fb2fe92d.png'}]
    }

    # Collecting answers
    answers = []
    message = await ctx.send("Starting test")
    for question in questions:
        await message.edit(content=f"{ctx.author.mention}, {question}")
        for emoji in options:
              await message.add_reaction(emoji)

        def check(reaction, user):
          return user == ctx.author and reaction.message.id == message.id and str(reaction.emoji) in options
        reaction, user = await bot.wait_for('reaction_add', check=check)
        answer = options.index(str(reaction.emoji)) + 1
        answers.append(answer)
        await message.clear_reactions()

    max_matches = 0
    matching_personality = "None"
    for personality, traits in personalities.items():
        matches = sum(a == b for a, b in zip(answers[:-1], traits[:-1]))
        if matches > max_matches:
            max_matches = matches
            matching_personality = personality
            matching_image = traits[-1]
    user_gender = 'male' if answers[-1] == 1 else 'female'  # Get the gender from last answer
    await ctx.send(f"Your personality type is closest to: {matching_personality}. Here is your persona:")
    await ctx.send(matching_image[user_gender])     
#time telling and gretting
@bot.command()
async def hi(ctx):
  timestamp = time.strftime('%H:%M:%S')
  await ctx.send("Time is")
  await ctx.send(timestamp)
  timestamp1 = time.strftime('%H')
  hour = int(timestamp1)
  if (hour > 12):
    if (hour > 15 and hour < 20):
      res = "Good evening have a warm tea and go see sunset!"
    elif (hour > 19 and hour <= 23):
      res = "Good nigth,have  great dinner and sleep well"
    elif (hour > 12 and hour < 16):
      res = "Good Afternoon, what are you doing?"
  else:
    if (hour > 5):
      res = "Good morning you early bird"
    if (hour < 5):
      res = "Good night, you are a night owl, you definitely need to go to bed"
  await ctx.send(res)

color_dict = {
    "❤️": "You're passionate and energetic.",
    "🧡": "You're adventurous and spontaneous.",
    "💛": "You're happy and creative.",
    "💚": "You're relaxed and nature-loving.",
    "💙": "You're calm and reliable.",
    "💜": "You're romantic and sensitive.",
    "🤎": "You're dependable and strong.",
    "🖤": "You're deep and introspective.",
    "🤍": "You're pure and peaceful."
}

month_dict = {
    "🔮": "You're inventive and unique (January/February - Aquarius).",
    "🐟": "You're compassionate and wise (February/March - Pisces).",
    "🐏": "You're courageous and enthusiastic (March/April - Aries).",
    "🐂": "You're dedicated and stubborn (April/May - Taurus).",
    "👬": "You're social and expressive (May/June - Gemini).",
    "🦀": "You're loyal and emotional (June/July - Cancer).",
    "🦁": "You're proud and outgoing (July/August - Leo).",
    "👧": "You're analytical and practical (August/September - Virgo).",
    "⚖️": "You're diplomatic and charming (September/October - Libra).",
    "🦂": "You're determined and powerful (October/November - Scorpio).",
    "🏹": "You're adventurous and philosophical (November/December - Sagittarius).",
    "🐐": "You're disciplined and patient (December/January - Capricorn)."
}

emoji_dict = {
    "😂": "You have a great sense of humor.",
    "❤️": "You're loving and warm-hearted.",
    "😍": "You're passionate and enthusiastic.",
    "🙏": "You're spiritual and thankful.",
    "😊": "You're positive and cheerful.",
    "💩": "You're humorous and don't take life too seriously.",
    "😘": "You're flirtatious and sociable.",
    "🔥": "You're energetic and ambitious.",
    "👍": "You're agreeable and supportive."
}

user_data = {}

@bot.command()
async def aboutme(ctx):
    user_data[ctx.author.id] = {
        "color": None,
        "month": None,
        "emoji": None
    }
    msg = await ctx.send("React with your favorite color!")
    for emoji in color_dict.keys():
        await msg.add_reaction(emoji)

@bot.event
async def on_reaction_add(reaction, user):
    if user == bot.user or user.id not in user_data:
        return

    emoji = str(reaction.emoji)
    message = reaction.message
    data = user_data[user.id]

    if emoji in color_dict.keys() and data["color"] is None:
        data["color"] = color_dict[emoji]
        await message.delete()
        msg = await message.channel.send("React with your birth month! \n🔮 is for January,\n 🐟 is for February, \n🐏 is for March, \n🐂 is for April, \n👬 is for May, \n🦀 is for June, 🦁 is for July, \n👧 is for August,\n ⚖️ is for September, \n🦂 is for October, \n🏹 is for November, \n 🐐 is for December")
        for emoji in month_dict.keys():
            await msg.add_reaction(emoji)
    elif emoji in month_dict.keys() and data["month"] is None:
        data["month"] = month_dict[emoji]
        await message.delete()
        msg = await message.channel.send("React with the emoji that represents you!")
        for emoji in emoji_dict.keys():
            await msg.add_reaction(emoji)
    elif emoji in emoji_dict.keys() and data["emoji"] is None:
        data["emoji"] = emoji_dict[emoji]
        await message.delete()
        await message.channel.send(f"{user.mention}, based on your choices: {data['color']}, {data['month']}, and {data['emoji']}!")
#info thing
@bot.command()
async def info(ctx):
  await ctx.send('!hi  To receive a Hello and  USA time with greeting ')
  await ctx.send('!start to take a simple personality test ')
  await ctx.send('!aboutme to know your traits')
bot.run(token)

