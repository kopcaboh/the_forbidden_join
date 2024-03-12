from browser import document



style = """
    width: 1.5vw;
    height: 1.5vw;
    background-color: #a1dadd;
    border: 2px solid #a1bcdd;
    border-radius: 2px;
    margin: 5px;
"""

def show():
    element = document.createElement('div')
    element.style.cssText = style

    return element
