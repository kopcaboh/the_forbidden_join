from browser import document, html, window
import memory_block.memory_block as memory_block
import memory.memory as memory
import table.table as table
from utils.utils import *
from frames import intro

root = document["root"]
content = document["content-container"]
screen_height = window.innerHeight
screen_width = window.innerWidth

def change_color():
    mem_block = document.select('.memory')[0]
    memory_block.mark_active(mem_block)

def change_color2():
    mem_block = document.select('.memory')[0]
    memory_block.mark_used(mem_block)

def set_timeout(ev):
    timer.set_timeout(change_color, 0)

def say_some_foolery():
    intro.present(content)


    # button = document.createElement('button')
    # button.appendChild(document.createTextNode('Color changer'))
    # button.style.alignSelf = "center"

    # chain = TimedEventChain()
    # chain.add(1000, change_color)
    # chain.add(1000, change_color2)

    # button.bind('click', chain.start_function)

    # block = memory_block.show()
    # block.classList.add('memory')

    # content.appendChild(block)
    # content.appendChild(button)

say_some_foolery()