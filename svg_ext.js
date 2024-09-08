(function svgExt(){
    htmx.defineExtension('svg-ext', {

        handleSwap: function(swapStyle, target, fragment, settleInfo) { 
            function add_children(target, node) {
                for (let child of node.children) {
                    add_child(target, child);
                }
            }
            function convertNS(fragment) {
                let newSVGContainer = document.createElementNS("http://www.w3.org/2000/svg", fragment.firstElementChild.tagName.toLowerCase());
                for (let attr of fragment.firstElementChild.attributes) {
                    newSVGContainer.setAttributeNS(null, attr.name, attr.value);
                }
                add_children(newSVGContainer, fragment.firstElementChild);
                return newSVGContainer;
            }
            function add_child(target, child) {
                let newSVG = document.createElementNS("http://www.w3.org/2000/svg", child.tagName.toLowerCase());
                for (let attr of child.attributes) {
                    newSVG.setAttributeNS(null, attr.name, attr.value);
                }
                target.appendChild(newSVG);
                
                // Copy text content if present
                if (child.childNodes.length > 0) {
                    for (let node of child.childNodes) {
                        if (node.nodeType === Node.TEXT_NODE) {
                            newSVG.appendChild(document.createTextNode(node.textContent));
                        } else if (node.nodeType === Node.ELEMENT_NODE) {
                            add_child(newSVG, node);
            }}}};
            // Check if fragment is not a DocumentFragment and wrap it if necessary
            if (!(fragment instanceof DocumentFragment)) {
                let tempFragment = document.createDocumentFragment();
                tempFragment.appendChild(fragment);
                fragment = tempFragment;
            }
            let newSVGContainer = convertNS(fragment);

            switch(swapStyle){
            case "innerSVG":
                while (target.firstChild) {
                    target.removeChild(target.firstChild);
                }
                target.appendChild(newSVGContainer);
                break;
            case "outerSVG":
                target.parentNode.replaceChild(newSVGContainer, target);
                target.remove()
                break;
            case "update":
                for (let attr of fragment.firstElementChild.attributes) {
                    target.setAttributeNS(null, attr.name, attr.value);
                }
                break;
            case "beforebeginSVG":
                target.parentNode.insertBefore(newSVGContainer, target)
                break;
            case "afterbeginSVG":
                target.insertBefore(newSVGContainer, target.firstChild)
                break;
            case "beforeendSVG":
                target.appendChild(newSVGContainer)
                break;
            case "afterendSVG":
                target.parentNode.insertBefore(newSVGContainer, target.nextSibling);
                break;
            case "deleteSVG":
                target.remove()
                break;
            default:
                return false
            }
            htmx.process(document.body)
            return true
        }})})();
