# SVG Extension for HTMX

This extension enhances HTMX functionality to work seamlessly with SVG elements, allowing for dynamic updates and interactions within SVG graphics. 

## Features

The SVG extension supports the following swap methods:

1. `innerSVG`: Updates the inner content of an SVG element.
2. `outerSVG`: Replaces an entire SVG element with new content.
3. `beforeendSVG`: Appends new SVG content to the end of the target element.
4. `deleteSVG`: Removes the target SVG element.
5. `beforebeginSVG`: Inserts new SVG content before the target element.
6. `afterbeginSVG`: Inserts new SVG content at the beginning of the target element.
7. `beforeendSVG`: Appends new SVG content to the end of the target element.
8. `afterendSVG`: Inserts new SVG content after the target element.
9. `deleteSVG`: Removes the target SVG element.


## Usage

To use the SVG extension, include the `svg_ext.js` script in your HTML and add the `hx-ext="svg-ext"` attribute to your SVG elements or their containers. Instead of the normal hx-swap options use one of the svg swaps to interact with SVGs. The rest of the htmx functionality should work as normal.

## Examples

To run the examples, you can use the following command:

```
python <example>
```

### 1. Inner SVG Swap (ex1.py)

This example demonstrates how to update the radius of a circle dynamically:

```
G(id="ex-innerSVG",  hx_ext="svg-ext", hx_swap="innerSVG",  hx_target="#ex-innerSVG",  hx_get="/innerSVG",hx_trigger="click")(...)
```
this activates the extension, specifies the swap method, the target element, the trigger, and the route.

### 2. Before End SVG Swap (ex2.py)

This example shows how to add new SVG elements using the `beforeendSVG` swap method:

```
G(id="ex-beforeEnd", hx_ext="svg-ext", hx_swap="beforeendSVG", hx_target="#ex-beforeEnd", hx_get="/beforeEnd",hx_trigger="click")
```

### 3. Outer SVG Swap (ex3.py)

This example demonstrates how to replace an entire SVG element with new content:

### 4. Out-of-Band Inner SVG Swap (ex4.py)

This example shows how to perform an out-of-band inner SVG swap, updating both the SVG and a button:
