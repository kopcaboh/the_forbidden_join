from browser import document, html

def highlight_row(n, table):
    rows = table.querySelectorAll('tr')
    row = rows[n+1] # Moving index to match python standard

    bounding_rect = row.getBoundingClientRect()
    highlight = html.IMG(src="/highlight.png",
                         height=bounding_rect.bottom - bounding_rect.top,
                         width=bounding_rect.right - bounding_rect.left)
    highlight.id = 'highlight'
    highlight.style.cssText = """
        position: absolute;
        z-index: -10;
    """

    print(f"top:{bounding_rect.top} left:{bounding_rect.left}")
    
    highlight.style.top = "%.4fpx" % bounding_rect.top
    highlight.style.left = "%.4fpx" % bounding_rect.left

    table.appendChild(highlight)
