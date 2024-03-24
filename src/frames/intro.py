from browser import document, html, window
from utils.utils import *

def layout():
    scene = document.createElement('div')
    scene.id = 'scene'
    scene.style.justifyContent = 'center'
    scene.style.alignItems = 'center'
    scene.style.textAlign = 'center'

    element = document.createElement('h1')
    element.appendChild(document.createTextNode("Nested loop join"))
    scene.appendChild(element)
    
    element = document.createElement('h2')
    element.appendChild(document.createTextNode("The default (brute force) algorithm"))
    scene.appendChild(element)

    element = document.createElement('button')
    element.appendChild(document.createTextNode("Continue >"))
    scene.appendChild(element)

    return scene

def present(stage):
    scene = layout()

    stage.appendChild(scene)
