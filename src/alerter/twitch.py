## added function for sending alert to twitch chat
from twitchio.ext import commands
import os

# set up the bot
bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'],
    nick=os.environ['BOT_NICK'],
    initial_channels=[os.environ['CHANNEL']]
)


@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/me has landed!")


def send_chat_alert(alertresponse, ctx):
    ctx.send(alertresponse)


bot.run()
