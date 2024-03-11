from browser import document, html

root = document["root"]

def say_some_foolery():
    new_tag = document.createElement("h1")
    new_text = document.createTextNode("Ahoj zlato")
    new_tag.appendChild(new_text)

    root.appendChild(new_tag)

say_some_foolery()