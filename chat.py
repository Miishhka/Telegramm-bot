from pyrogram import Client, filters
import config
app = Client(
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    name="my_bot"
)

waiting = []
pairs = {}

@app.on_message(filters.command("start"))
async def start(_, message):
    user_id = message.from_user.id

    if waiting:
        partner = waiting.pop(0)
        pairs[user_id] = partner
        pairs[partner] = user_id

        await app.send_message(user_id, "Собеседник найден!")
        await app.send_message(partner, "Собеседник найден!")
    else:
        waiting.append(user_id)
        await message.reply("Ждём второго пользователя...")
@app.on_message()
async def chat(_, message):
    uid = message.from_user.id

    if uid in pairs:
        await message.copy(pairs[uid])


app.run()
