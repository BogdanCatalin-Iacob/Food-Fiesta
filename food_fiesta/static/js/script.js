document.addEventListener('DOMContentLoaded', function() {
  // mobile nav initialization
    let sidenav = document.querySelectorAll('.sidenav');
    M.Sidenav.init(sidenav);

    //collapsible component initialization
    let elems = document.querySelectorAll('.collapsible');
    let instances = M.Collapsible.init(elems);
  });