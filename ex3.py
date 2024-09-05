from fasthtml.common import *
from fasthtml.svg import *
from fasthtml.components import Script
import random

app, rt = fast_app(live=True, hdrs=[Script(src="svg_ext.js")])


def outerSVG(shape):
    if shape == "circle":
        return Circle(cx=15, cy=15, r=10, fill="red",id="ex-outerSVG-2")(
            hx_ext="svg-ext", hx_swap="outerSVG", hx_target="#ex-outerSVG-2", hx_get="/outerSVG/rect",hx_trigger="click")
    elif shape == "rect":
        return Rect(x=10, y=10, width=10, height=10, fill="blue",id="ex-outerSVG-2")(
            hx_ext="svg-ext", hx_swap="outerSVG", hx_target="#ex-outerSVG-2", hx_get="/outerSVG/circle",hx_trigger="click")


@app.get('/')
def homepage():
    return Div(
        P("click the object to swap it with outerSVG"),
        Svg(xmlns="http://www.w3.org/2000/svg", viewBox="0 0 150 100", id="svg-box")(
            G(id="ex-outerSVG")(outerSVG("rect")),
        ),
    )

@rt("/outerSVG/{shape}")
def get(shape: str):
    return outerSVG(shape)

serve()