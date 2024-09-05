from fasthtml.common import *
from fasthtml.svg import *
from fasthtml.components import Script
import random

app, rt = fast_app(live=True, hdrs=[Script(src="svg_ext.js")])

def innerSVG(): return Circle(cx=15, cy=10, r=random.randint(1,10), fill="red")

@app.get('/')
def homepage():
    return Div(
        P("Click the object to do an inner SVG swap - change the circle's radius"),
        Svg(xmlns="http://www.w3.org/2000/svg", viewBox="0 0 150 100", id="svg-box")(
            G(id="ex-innerSVG",  hx_ext="svg-ext", hx_swap="innerSVG",  hx_target="#ex-innerSVG",  hx_get="/innerSVG",hx_trigger="click")(innerSVG()),
    ))

@rt("/innerSVG")
def get():
    return innerSVG()

serve()