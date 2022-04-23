"""
Asynchronous IO (async IO): a language-agnostic paradigm (model) that has implementations across a host of programming languages
async/await: two new Python keywords that are used to define coroutines
asyncio: the Python package that provides a foundation and API for running and managing coroutines
Coroutines (specialized generator functions) are the heart of async IO in Python, and we’ll dive into them later on.

The asyncio package is billed by the Python documentation as a library to write concurrent code.
However, async IO is not threading, nor is it multiprocessing. It is not built on top of either of these.
In fact, async IO is a single-threaded, single-process design: it uses cooperative multitasking.

It has been said in other words that async IO gives a feeling of concurrency despite using a single thread in a single process.
Coroutines (a central feature of async IO) can be scheduled concurrently, but they are not inherently concurrent.
"""

"""
Asynchronous routines are able to “pause” while waiting on their ultimate result and let other routines run in the meantime.
The syntax async def introduces either a native coroutine or an asynchronous generator. 

The keyword await passes function control back to the event loop. (It suspends the execution of the surrounding coroutine.) 
If Python encounters an await f() expression in the scope of g(), this is how await tells the event loop, 
“Suspend execution of g() until whatever I’m waiting on—the result of f()—is returned. In the meantime, 
go let something else run.”
"""

"""
A function that you introduce with async def is a coroutine. It may use await, return, or yield, 
but all of these are optional. Declaring async def f(): pass is valid:

Using await and/or return create a coroutine function. To call a coroutine function,you must await it to get its result.
"""

import asyncio


async def fetch_data():
    print('Start fetching')
    await asyncio.sleep(2)
    print('done fetching')


async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)


async def main():
    task1 = asyncio.create_task(print_numbers())
    await fetch_data()
    await task1


asyncio.run(main())
