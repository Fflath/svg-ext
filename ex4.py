from fasthtml.common import *
from fasthtml.svg import *
from fasthtml.components import Script
import random

app, rt = fast_app(live=True, hdrs=[Script(src="svg_ext.js")])

def oobinnerSVG():
    return Circle(cx=15, cy=15, r=random.randint(1,10), fill="red")

def mk_oob_innerSVG_button(count: int):
    return Button(id="oob-innerSVG-button" + str(count),hx_ext="svg-ext", hx_swap="outerHTML", hx_target="#oob-innerSVG-button" + str(count), hx_get="/oob/innerSVG/" + str(count))("innerSVG-oob: " + str(count) + " clicks")


@app.get('/')
def homepage():
    return Div(
        P("Click the button to do an oob innerSVG swap. Updates the svg and the button"),
        mk_oob_innerSVG_button(0),
        Svg(xmlns="http://www.w3.org/2000/svg", viewBox="0 0 150 100", id="svg-box")(
            G(id="ex-innerSVG-oob", hx_ext="svg-ext"),
        ),
    )

@rt("/oob/innerSVG/{count}")
def get(count: int):
    return mk_oob_innerSVG_button(count+1),oobinnerSVG()(hx_ext="svg-ext", hx_target="#ex-innerSVG-oob",hx_swap_oob="innerSVG:#ex-innerSVG-oob")

serve()