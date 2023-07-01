import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ChatPermissions
from datetime import timedelta

API_TOKEN = '6215191160:AAGkFHh-PzRemw__sV44Ni6CcwtS8tLleEw'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hello")


@dp.message_handler(commands="mute", is_chat_admin=True)
async def mute_user(message: types.Message):
    if message.chat.type in ["group", "supergroup"]:
        if not message.reply_to_message or not message.reply_to_message.from_user:
            await message.reply("Iltimos, biror kishini belgilab keyin komandani yuboring")
            return
        
        user_to_mute = message.reply_to_message.from_user
        await bot.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=user_to_mute.id,
            permissions=ChatPermissions(
            can_send_messages=False,
            ),
            until_date=message.date + timedelta(minutes=30)
        )
        
        await message.reply(f"{user_to_mute.mention} you are muted for 30 minutes, lox")



@dp.message_handler(text="/unmute", is_chat_admin=True)
async def unmute_user(message: types.Message):
    if message.chat.type in ["supergroup", "group"]:
        if not message.reply_to_message or not message.reply_to_message.from_user:
            await message.reply("Iltimos, biror kishini belgilab keyin komandani yuboring")
            return
        
        user_to_unmute = message.reply_to_message.from_user
        await bot.restrict_chat_member(
            chat_id=message.chat.id,
            user_id=user_to_unmute.id,
            permissions=ChatPermissions(
            can_send_messages=True,
            ),
            until_date=0
        )
        


@dp.message_handler(text="!ban", is_chat_admin=True)
async def unmute_user(message: types.Message):
    if message.chat.type in ["supergroup", "group"]:
        if not message.reply_to_message or not message.reply_to_message.from_user:
            await message.reply("Iltimos, biror kishini belgilab keyin komandani yuboring")
            return
        
        user_to_ban = message.reply_to_message.from_user
        await bot.kick_chat_member(
            chat_id=message.chat.id,
            user_id=user_to_ban.id,
        )
        await message.reply(f"{user_to_ban.mention} bomj, туда тебя")

        

@dp.message_handler(text="!unban", is_chat_admin=True)
async def unmute_user(message: types.Message):
    if message.chat.type in ["supergroup", "group"]:
        if not message.reply_to_message or not message.reply_to_message.from_user:
            await message.reply("Iltimos, biror kishini belgilab keyin komandani yuboring")
            return
        
        user_to_unban = message.reply_to_message.from_user
        await message.chat.unban(user_to_unban.id)

        await message.reply(f"{user_to_unban.mention} cum back bomj")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)



# @dp.message_handler(commands=['unmute'])
# async def unmute_user(message: types.Message):
#     chat_id = message.chat.id
#     user_id = message.reply_to_message.from_user.id
#     permissions = types.ChatPermissions(mute_members=False)
#     await bot.restrict_chat_member(chat_id, user_id, permissions)
#     await message.reply_text('User unmuted successfully!')
