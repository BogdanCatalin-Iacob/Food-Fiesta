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
function addIngredient() {
  let ingredientsList = document.getElementById("ingredientsList");
  // show the field if hidden
  if (ingredientsList.classList.contains("hide")) {
    ingredientsList.classList.remove("hide");
  }

  // add items to the ingredients list
  let ingredients = [];
  let ingredient = document.getElementById("ingredients").value;
  ingredients.push(ingredient);
  document.getElementById("ingredients").value = "";

  // display all the items from the ingredients list
  ingredients.forEach(item => {
    document.getElementById("ingredientsList").innerHTML += `<input disabled class="col s12 m4 l3" type="text" value="${item}">`
  });
}
let stepCount = 1;

function addStep() {
  let stepList = document.getElementById("stepsList");
  // show the firld if hidden
  if (stepList.classList.contains("hide")) {
    stepList.classList.remove("hide");
  }

  let stepsList = {}
  let stepValue = document.getElementById("steps").value;
  stepsList[stepCount] = stepValue;
  document.getElementById("steps").value = "";
  stepCount++;
  document.getElementById("prep_step").innerText = `Preparation step ${stepCount}`;

  for (step in stepsList) {
    document.getElementById("stepsList").innerHTML += `<p class="col s2">Step ${step}: 
      </p><textarea disabled class="materialize-textarea">${stepsList[step]}</textarea>`
  }
}

// add ingredient and steps buttons event listeners
let addButton = document.getElementById("addButton");
let addStepButton = document.getElementById("addStepButton");

addButton.addEventListener("click", addIngredient);
addStepButton.addEventListener("click", addStep);