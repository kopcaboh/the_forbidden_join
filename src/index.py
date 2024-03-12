from browser import document, html, window

root = document["root"]
screen_height = window.innerHeight
screen_width = window.innerWidth

def say_some_foolery():
    svg_canvas = document.createElement("svg")
    # svg_canvas = svg.svg(x=0, y=0,
    #                      width=window.width, height=window.height,
    #                      fill="blue")
    new_tag = document.createElement("h1")
    new_text = document.createTextNode("Hello world")
    new_tag.appendChild(new_text)

    root.appendChild(new_tag)
    root.appendChild(svg_canvas)

say_some_foolery()