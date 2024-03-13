from browser import document
import memory_block.memory_block as memory_block

MEM_SIZE = 9 #blocks

logo_style = """
    height: 120px;
    width: 120px;

    position: absolute;
    left: 50%;
    right: 50%;
    margin-left: calc(-60px + 10px);
    margin-top: calc(-60px - 10px - 30px);
"""

outer_blocks_container_style = """
    display: grid;
    grid-template-columns: repeat(3, 1fr);
"""

insides_style = """
    margin-top: 20px;

    display: grid;
    grid-template-columns: 3fr 1fr 1fr;
    grid-gap: 30px;
"""

outsides_style = """
    background-color: white;

    border: solid black 10px;
    border-radius: 50px / 50px;

    padding: 30px;
    margin: 10px;
"""

def make_insides():
    insides = document.createElement('div')
    insides.style.cssText = insides_style

    outer_blocks = [memory_block.show() for i in range(MEM_SIZE - 2)]
    outer_blocks_container = document.createElement('div')
    outer_blocks_container.style.cssText = outer_blocks_container_style
    for block in outer_blocks:
        outer_blocks_container.appendChild(block)

    insides.appendChild(outer_blocks_container)


    inner_blocks = memory_block.show()
    insides.appendChild(inner_blocks)


    output_blocks = memory_block.show()
    insides.appendChild(output_blocks)

    # insides.style.backgroundColor = 'blue'
    # insides.style.height = '300px'
    # insides.style.width = '400px'

    return insides


def make_container():
    outsides = document.createElement('div')
    outsides.id = 'memory'
    outsides.style.cssText = outsides_style

    logo = document.createElement('img')
    logo.src = '/processor.svg'
    logo.alt = 'Processor'
    logo.style.cssText = logo_style
    outsides.appendChild(logo)

    insides = make_insides()
    outsides.appendChild(insides)

    element = outsides

    return element


def show():
    element = make_container()

    return element
