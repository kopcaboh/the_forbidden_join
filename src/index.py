from browser import document, html, window

root = document["root"]
screen_height = window.innerHeight
screen_width = window.innerWidth

def say_some_foolery():
    new_tag = document.createElement("h1")
    new_text = document.createTextNode("Hello world")
    new_tag.appendChild(new_text)

    root.appendChild(new_tag)

say_some_foolery()