from browser import document, html, window
import memory_block.memory_block as memory_block
import memory.memory as memory

root = document["root"]
screen_height = window.innerHeight
screen_width = window.innerWidth

def say_some_foolery():
    element = memory.show()

    root.appendChild(element)

say_some_foolery()