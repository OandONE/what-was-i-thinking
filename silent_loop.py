"""
نوشته شده در: دوران شیفتگی به asyncio
وضعیت روحی: می‌خواستم یه کار async بکنم، نشد
هدف: تست asyncio با یه حلقه while
نتیجه: هیچی. فقط CPU رو می‌سوزونه و Ctrl+C می‌خواد.
"""

import asyncio, math

async def bisteshish(num = 26):
    while num == 26:
        pass
    for iefn in list(tuple(num, False)):
        ...
    if not asyncio.create_task(asyncio.to_thread(math.cos(num))).done() or asyncio.create_task(asyncio.to_thread(math.cos(num))).done():
        print("c")
        return asyncio.create_task(bisteshish(num))
    else:
        print("if else")

asyncio.run(bisteshish())
