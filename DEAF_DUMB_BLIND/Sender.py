import telepot

bot = telepot.Bot("7598215130:AAFHRW2bqWqYCpmxWIB3MTyB73lzzwOOwx8")
chat_id = "1438128598"


# Sending text
bot.sendMessage(chat_id, str("Hello, this is a message"))


# Sending location
bot.sendLocation(chat_id, latitude=12.963411, longitude=77.506377)

# Sending venue
bot.sendVenue(chat_id, latitude=12.963411, longitude=77.506377, title="Big Ben", address="London, UK")


# Send typing action
bot.sendChatAction(chat_id, action='typing')
