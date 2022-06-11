document.addEventListener('DOMContentLoaded', function () {
  // mobile nav initialization
  let sidenav = document.querySelectorAll('.sidenav');
  M.Sidenav.init(sidenav);

  // collapsible component initialization (recipes)
  let elems = document.querySelectorAll('.collapsible');
  let instances = M.Collapsible.init(elems);

  // select list initialization (create_recipe)
  let list_elems = document.querySelectorAll('select');
  let list_instances = M.FormSelect.init(list_elems);
  totalTime();
});

/**
 * update the create_recipe form total time by adding cook_time and prep_time
 */
function totalTime() {
  // get the values from the form
  let cookTime = parseInt(document.getElementById("cook_time").value);
  let prepTime = parseInt(document.getElementById("prep_time").value);
  let totalTime = 0;

  // check if is any value in the fields
  if (cookTime >= 0 && prepTime >= 0) {
    totalTime = cookTime + prepTime;
  } else if (cookTime >= 0) {
    totalTime = cookTime;
  } else if (prepTime >= 0) {
    totalTime = prepTime;
  }

  document.getElementById("total_time").value = totalTime;
}

/**
 * Add ingredients to the list and display them
 */
function addIngredient(){
  let ingredientsList = document.getElementById("ingredientsList");
  // show the field if hidden
  if (ingredientsList.classList.contains("hide")){
    ingredientsList.classList.remove("hide");
  }

  // add items to the ingredients list
  let ingredients = [];
  let ingredient = document.getElementById("ingredients").value;
  ingredients.push(ingredient);
  document.getElementById("ingredients").value = "";

  // display all the items from the ingredients list
  ingredients.forEach(item => {document.getElementById("ingredientsList").innerHTML += `<input class="col s11 m4 l3" type="text" value="${item}">`});
}

// add ingredient button event listener
let addButton = document.getElementById("addButton");
addButton.addEventListener("click", addIngredient);
