from browser import document, html
import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"top: {self.y}, left: {self.x}"
    
    def __repr__(self):
        return f"{(self.x, self.y)}"

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def __mul__(self, x):
        return Point(self.x * x, self.y * x)
    
    def __truediv__(self, x):
        return Point(self.x / x, self.y / x)
    
    def __truediv__(self, x):
        return Point(self.x // x, self.y // x)

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def distance(self, p):
        diff = p - self
        return math.hypot(diff.x, diff.y)
    
    def angle(self, p):
        '''Angle in radians from left-right horizontal'''
        angle = math.atan2(p.y - self.y, p.x - self.x)
        return angle

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

    # print(f"top:{bounding_rect.top} left:{bounding_rect.left}")
    
    highlight.style.top = "%.4fpx" % bounding_rect.top
    highlight.style.left = "%.4fpx" % bounding_rect.left

    table.appendChild(highlight)

def connect_points(first, second):
    first_is_pivot = True
    if first.x > second.x:
        first_is_pivot = False
        print("Swapping pivots")
    elif first.x == second.x and first.y > second.y:
        first_is_pivot = False
        print("Swapping pivots")

    pivot = first if first_is_pivot else second
    follow = second if first_is_pivot else first

    angle = pivot.angle(follow) # radians
    length = pivot.distance(follow)
    

    line_style = """
        position: absolute;
        border-top: 1px solid #000;
        transform-origin: left;
    """

    line = document.createElement('div')
    line.style.cssText = line_style
    line.style.left = "%.4fpx" % pivot.x
    line.style.top = "%.4fpx" % pivot.y
    line.style.width = "%.4fpx" % length
    line.style.transform = "rotate(%frad)" % angle

    # print("angle: %.3f  length: %.3f" % (angle, length))

    document["root"].appendChild(line)


def connect_table_with_block(table, block, table_offset=0):
    pass

if __name__ == "__main__":
    a = Point(0, 0)
    b = Point(60, 20)
    print(connect_points(a, b))
