document.addEventListener('DOMContentLoaded', function () {
  // mobile nav initialization
  let sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenav);

  // collapsible component initialization (recipes)
  let elems = document.querySelectorAll('.collapsible');
  M.Collapsible.init(elems);

  // select list initialization (create_recipe)
  let list_elems = document.querySelectorAll('select');
  M.FormSelect.init(list_elems);

  let modalElems = document.querySelectorAll('.modal');
  M.Modal.init(modalElems);

});