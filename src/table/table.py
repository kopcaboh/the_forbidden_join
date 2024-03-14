from browser import document
from browser.html import TABLE, TR, TH, TD


pobocky = [
    ("ID", "Město", "Adresa"),
    (1, "Praha", "adresa"),
    (2, "Brno", "adresa"),
    (3, "Plzeň", "adresa"),
    (4, "Jihlava", "adresa"),
    (5, "Ostrava", "adresa")
]

zamestnanci = [
    ("ID", "Jméno", "Pobočka"),
    (1, "Pavel Ředkvička", "adresa"),
    (2, "Martin Tykev", "adresa"),
    (3, "Aleš Kedluben", "adresa"),
    (4, "Zita Ořechová", "adresa"),
    (5, "David Kořen", "adresa"),
    (6, "Vlastimil Jahoda", "adresa"),
    (7, "Emma Brukvová", "adresa"),
]

table_style = """
    border: 1.5px solid black;
    border-collapse: collapse;

    font-family: Arial, sans-serif;
"""

tr_style = """

"""

th_style = """
    border: 1px solid black;
    padding: 0.5rem;
"""

td_style = """
    padding: 0.5rem;
    padding-right: 1rem;
"""

number_td_style = """
    text-align: right;
"""

def show_table_data(data):
    table = TABLE()

    #header
    table.appendChild(
        TR(TH(col_header) for col_header in data[0])
    )

    #data
    for record in data[1:]:
        table.appendChild(
            TR(TD(column) for column in record)
        )

    #styling
    table.style.cssText = table_style
    for element in table.querySelectorAll('tr'):
        element.style.cssText = tr_style

    for element in table.querySelectorAll('th'):
        element.style.cssText = th_style

    for element in table.querySelectorAll('td'):
        element.style.cssText = td_style

    for row in table.querySelectorAll('tr'):
        row.children[0].style.cssText += number_td_style

    return table





def show(data=zamestnanci):
    wrapper = document.createElement('div')
    wrapper.id = 'table'

    wrapper.appendChild(show_table_data(data=data))

    element = wrapper

    return element
