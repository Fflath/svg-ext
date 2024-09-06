from fasthtml.common import *
from fasthtml.svg import *
from fasthtml.components import Script
import random

app, rt = fast_app(live=True, hdrs=[Script(src="svg_ext.js")])

be_count = 0

def innerSVG():
    return Circle(cx=15, cy=10, r=random.randint(1,10), fill="red")

def beforeEnd():
    global be_count
    be_count += 1
    return Rect(x=10+10*be_count, y=30, width=10, height=10, fill="blue")

def outerSVG(shape):
    if shape == "circle":
        return Circle(cx=15, cy=55, r=10, fill="red",id="ex-outerSVG-2")(
            hx_ext="svg-ext", hx_swap="outerSVG", hx_target="#ex-outerSVG-2", hx_get="/outerSVG/rect",hx_trigger="click")
    elif shape == "rect":
        return Rect(x=10, y=50, width=10, height=10, fill="blue",id="ex-outerSVG-2")(
            hx_ext="svg-ext", hx_swap="outerSVG", hx_target="#ex-outerSVG-2", hx_get="/outerSVG/circle",hx_trigger="click")


@app.get('/')
def homepage():
    global be_count
    be_count = -1
    return Div(
        mk_oob_innerSVG_button(0),
        Svg(xmlns="http://www.w3.org/2000/svg", viewBox="0 0 150 100", id="svg-box")(
            G(id="ex-innerSVG",  hx_ext="svg-ext", hx_swap="innerSVG",  hx_target="#ex-innerSVG",  hx_get="/innerSVG",hx_trigger="click")(innerSVG()),
            G(id="ex-beforeEnd", hx_ext="svg-ext", hx_swap="beforeendSVG", hx_target="#ex-beforeEnd", hx_get="/beforeEnd",hx_trigger="click")(beforeEnd()),
            G(id="ex-outerSVG")(outerSVG("rect")),
            G(id="ex-innerSVG-oob", hx_ext="svg-ext"),
            G(id="ex-deleteSVG", hx_ext="svg-ext")(Rect(x=40, y=5, width=10, height=10, fill="blue")(
                hx_swap="deleteSVG", hx_target="#ex-deleteSVG",hx_trigger="click", hx_get="/deleteSVG"
            ))
        ),
    )

@rt("/innerSVG")
def get():
    return innerSVG()

@rt("/beforeEnd")
def get():
    return beforeEnd()

@rt("/outerSVG/{shape}")
def get(shape: str):
    return outerSVG(shape)


def oobinnerSVG():
    return Circle(cx=15, cy=70, r=random.randint(1,10), fill="red")

def mk_oob_innerSVG_button(count: int):
    return Button(id="oob-innerSVG-button",hx_ext="svg-ext", hx_swap="outerHTML", hx_target="#oob-innerSVG-button" , hx_get=f"/oob/innerSVG/{count}")(f"innerSVG-oob: {count} clicks")
@rt("/oob/innerSVG/{count}")
def get(count: int):
    return mk_oob_innerSVG_button(count+1),oobinnerSVG()(hx_ext="svg-ext", hx_target="#ex-innerSVG-oob",hx_swap_oob="innerSVG:#ex-innerSVG-oob")

@rt("/deleteSVG")
def get():
    return Rect(x=40, y=5, width=10, height=10, fill="blue")

serve()