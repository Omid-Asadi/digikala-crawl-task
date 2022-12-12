var formatter = new Intl.NumberFormat("fa-IR");
var $ = jQuery;
function insertAfter(referenceNode, newNode) {
  referenceNode.parentNode.insertBefore(
    newNode,
    referenceNode.nextSibling
  );
}
$(document).ready(function () {
  var items = $('input[type="number"]');
  for (var i = 0; i < items.length; i++) {
    var el = document.createElement("span");
    el.setAttribute("id", items[i].name);
    el.classList.add("amounts");
    insertAfter(items[i], el);
  }
  items.keyup(function (e) {
    var elements = document.getElementById(this.name);
    elements.innerHTML = formatter.format(this.value);
  });
});
