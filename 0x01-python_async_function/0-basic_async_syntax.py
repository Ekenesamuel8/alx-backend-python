#!/usr/bin/env python3
"""asynchronous coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> int:
    """wait_random
    args:
        random.uniform(0, max_delay):
    generates a random floating-point number between 0 and max_delay.
    delay: is a floating-point number representing the number
      of seconds to sleep
    await asyncio.sleep(delay): pauses the execution of the wait_random
     coroutine for the amount of time specified by delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
