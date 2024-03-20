from browser import document, html, window
from memory_block.memory_block import *
import memory.memory as memory
import table.table as table
from utils.utils import *

root = document["root"]
content = document["content-container"]
screen_height = window.innerHeight
screen_width = window.innerWidth

def say_some_foolery():
    memblocks = [show() for i in range(10)]
    
    for i in range(0, 3):
        mark_used(memblocks[i])
        
    for i in range(3, 7):
        mark_active(memblocks[i])


    for memblock in memblocks:
        content.appendChild(memblock)

      

say_some_foolery()