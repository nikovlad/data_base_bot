import os
import requests
import config
import asyncio
from bs4 import BeautifulSoup as BS

passport_file_name = "test.json"

def main():
    while True:
        if(os.path.exists("passports.db")):
            print("База данных на месте")
        else:
            print("База данных отсутствует")
        loop = asyncio.get_event_loop()
        loop.create_task(notification(10))

async def notification(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        if (os.path.exists("passports.db")):
            print("будет выполняться парисинг")
        else:
            print("\nуведомления никто не получит")

if __name__ == '__main__':
    main()
