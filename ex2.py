from fasthtml.common import *
from fasthtml.svg import *
from fasthtml.components import Script

app, rt = fast_app(live=True, hdrs=[Script(src="svg_ext.js")])

be_count = 0

def beforeEnd():
    global be_count
    be_count += 1
    return Rect(x=10+10*be_count, y=30, width=10, height=10, fill="blue")

@app.get('/')
def homepage():
    global be_count
    be_count = -1
    return Div(
        P("Click the rectangle to add another svg next to the current one using beforeendSVG"),
        Svg(xmlns="http://www.w3.org/2000/svg", viewBox="0 0 150 100", id="svg-box")(
            G(id="ex-beforeEnd", hx_ext="svg-ext", hx_swap="beforeendSVG", hx_target="#ex-beforeEnd", hx_get="/beforeEnd",hx_trigger="click")(beforeEnd()),
        ),
    )

@rt("/beforeEnd")
def get():
    return beforeEnd()

serve()