#!/usr/bin/env python

import asyncio
import telegram

from config import TOKEN

async def main():
    bot = telegram.Bot(TOKEN)
    async with bot:
        print((await bot.get_updates())[0])

asyncio.run(main())