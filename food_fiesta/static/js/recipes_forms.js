document.addEventListener("DOMContentLoaded", function(){
    // validate choose category
    validateMaterializeSelect();
});

// form add element buttons
let addButton = document.getElementById("addButton");
let addStepButton = document.getElementById("addStepButton");

// count the steps for preparation
let stepCount = 1;

// code credit: [codeinstitute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+DCP101+2017_T3/courseware/9e2f12f5584e48acb3c29e9b0d7cc4fe/6449dcd23ca14016aa83dc7313d91a02/?child=first)
/**
 * Make the Category Choose be mandatory before submitting the form
 */
function validateMaterializeSelect() {
  let classValid = "border-bottom: 1px solid #4caf50; box-shadow: 0 1px 0 0 #4caf50;";
  let classInvalid = "border-bottom: 1px solid #f44336; box-shadow: 0 1px 0 0 #f44336;";
  let selectValidate = document.querySelector("select.validate");
  let selectWrapperInput = document.querySelector(".select-wrapper input.select-dropdown");
  if (selectValidate.hasAttribute("required")) {
    selectValidate.style.cssText = "display: block; height: 0; padding: 0; width: 0; position: absolute;";
  }
  selectWrapperInput.addEventListener("focusin", (e) => {
    e.target.parentNode.addEventListener("change", () => {
      ulSelectOptions = e.target.parentNode.childNodes[1].childNodes;
      for (let i = 0; i < ulSelectOptions.length; i++) {
        if (ulSelectOptions[i].className == "selected" && ulSelectOptions[i].hasAttribute != "disabled") {
          e.target.style.cssText = classValid;
        }
      }
    });
  });
  selectWrapperInput.addEventListener("click", (e) => {
    ulSelectOptions = e.target.parentNode.childNodes[1].childNodes;
    for (let i = 0; i < ulSelectOptions.length; i++) {
      if (ulSelectOptions[i].className == "selected" && ulSelectOptions[i].hasAttribute != "disabled" && ulSelectOptions[i].style.backgroundColor == "rgba(0, 0, 0, 0.03)") {
        e.target.style.cssText = classValid;
      } else {
        e.target.addEventListener("focusout", () => {
          if (e.target.parentNode.childNodes[3].hasAttribute("required")) {
            if (e.target.style.borderBottom != "1px solid rgb(76, 175, 80)") {
              e.target.style.cssText = classInvalid;
            }
          }
        });
      }
    }
  });
}
// end of Category validation

/**
 * Add ingredients to the list and display them
 */
function addIngredient() {
  let emptyField = document.getElementById("empty-field");
  let ingredientsList = document.getElementById("ingredients-list");

  // delete empty field message from display
  emptyField.classList.add("hide");

  // show the field if hidden
  if (ingredientsList.classList.contains("hide")) {
    ingredientsList.classList.remove("hide");
  }

  let ingredient = document.getElementById("ingredients").value;

  // check if the input field has any value
  if (ingredient == null || ingredient == "") {
    // show error message if empty field 
    emptyField.classList.remove("hide");
  } else {
    document.getElementById("ingredients").value = "";
    document.getElementById("ingredients-list").innerHTML += `<input type="text" name="ingredientsList" value="${ingredient}">`;
  }
}

/**
 * add preparation steps into an object and displays it on the screen
 */
function addStep() {
  let emptyFieldPrep = document.getElementById("empty-field-prep");
  let stepList = document.getElementById("steps-list");

  // delete empty field message from display
  emptyFieldPrep.classList.add("hide");

  // show the fields if hidden
  if (stepList.classList.contains("hide")) {
    stepList.classList.remove("hide");
  }

  let stepValue = document.getElementById("steps").value;

  if (stepValue == null || stepValue == "") {
    // show error message if empty field 
    emptyFieldPrep.classList.remove("hide");
  } else {
    // add properties to object
    document.getElementById("steps").value = ""; // clear the typed in text
    // display the inserted values on the screen above input field
    stepList.innerHTML += `<span>Step ${stepCount}</span><textarea type="text" name="stepsList">${stepValue}</textarea>`;
    stepCount++;
    document.getElementById("prep-step").innerText = `Preparation step ${stepCount}`;
  }
}

// add ingredient and steps buttons event listeners
addButton.addEventListener("click", addIngredient);
addStepButton.addEventListener("click", addStep);