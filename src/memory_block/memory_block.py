from browser import document



style = """
    width: 1.5vw;
    height: 1.5vw;
    border-width: 2px;
    border-style: solid;
    border-radius: 2px;
    margin: 5px;
"""

def mark_normal(mem_block):
    mem_block.style.backgroundColor = "#D7CB84"
    mem_block.style.borderColor = "#CDBD65"

def mark_active(mem_block):
    mem_block.style.backgroundColor = "#E07A5F"
    mem_block.style.borderColor = "#DB6443"

def mark_used(mem_block):
    mem_block.style.backgroundColor = "#928FB7"
    mem_block.style.borderColor = "#7976A7"

def show():
    element = document.createElement('div')
    element.style.cssText = style
    mark_normal(element)

    return element
