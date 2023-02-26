import os
import aiohttp
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from config import TOKEN


# Create a bot instance and initialize the dispatcher
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(content_types=['document'])
async def process_file(message: Message):
    # Get the document file id
    file_id = message.document.file_id

    # Download the file to a temporary directory
    file_path = await bot.get_file(file_id)
    file_path = f'https://api.telegram.org/file/bot{TOKEN}/{file_path.file_path}'
    file_name = message.document.file_name
    try:
        first_name = message.forward_from.first_name
        last_name = message.forward_from.last_name
        folder_name = f'{first_name}_{last_name}'
    except AttributeError:
        folder_name = 'my'
    if not os.path.isdir(folder_name):
        os.mkdir(folder_name)
    async with aiohttp.ClientSession() as session:
        async with session.get(file_path) as resp:
            with open(f'{folder_name}/{file_name}', 'wb') as f:
                f.write(await resp.read())

    # Clear the state and send a confirmation message
    # await state.finish()
    await message.answer(f'The file {file_name} has been saved.')


if __name__ == '__main__':
    # Start the bot
    asyncio.run(dp.start_polling())
