from browser import document, html, window
from utils.utils import *

def present(stage):
    scene = document.createElement('div')
    scene.id = 'scene'
    scene.style.justifyContent = 'center'
    scene.style.alignItems = 'center'
    scene.style.textAlign = 'center'

    element = document.createElement('h1')
    element.appendChild(document.createTextNode("Nested loop join"))
    element.classList.add('fade-in')
    element.style.animationDelay = "0ms"
    scene.appendChild(element)
    
    element = document.createElement('h2')
    element.appendChild(document.createTextNode("The default (brute force) algorithm"))
    element.classList.add('fade-in')
    element.style.animationDelay = "500ms"
    scene.appendChild(element)

    element = document.createElement('button')
    element.appendChild(document.createTextNode("Continue >"))
    element.classList.add('fade-in')
    element.style.animationDelay = "1000ms"
    scene.appendChild(element)
    
    stage.appendChild(scene)
