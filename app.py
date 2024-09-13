from loader import bot, dp
import handlers, middlewares
from utils.notify_admins import start,shutdown
from aiogram.types.bot_command_scope_all_private_chats import BotCommandScopeAllPrivateChats
from utils.set_botcommands import commands
#from middlewares.test import CounterMiddleware
#from middlewares.mymiddleware import UserCheckMiddleware
import logging
import sys
import asyncio

async def main():
    try:
        await bot.delete_webhook(drop_pending_updates=True)
        await bot.set_my_commands(commands=commands,scope=BotCommandScopeAllPrivateChats(type='all_private_chats'))
        dp.startup.register(start)
        dp.shutdown.register(shutdown)
        #dp.message.middleware(CounterMiddleware())
        #dp.message.middleware(UserCheckMiddleware())
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
if __name__=='__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())