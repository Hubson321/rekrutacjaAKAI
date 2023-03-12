let firstName = document.getElementById("firstName"),
  email = document.getElementById("email"),
  lastName = document.getElementById("lastName"),
  form = document.getElementById("form"),
  
  errorMsg = document.getElementsByClassName("error"),
  frontendCheckbox = document.getElementById('frontend-checkbox'),
  mobileCheckbox = document.getElementById('mobile-checkbox'),
  graphicsCheckbox = document.getElementById('graphics-checkbox')
  backendCheckbox = document.getElementById('backend-checkbox');

  let formValid = 0;

  form.addEventListener("submit", (e) => {
    e.preventDefault();

    engine(firstName, 0, "Imie nie może być puste");
    engine(lastName, 1, "Nazwisko nie może byc puste");
    engine(email, 2, "Adres email nie może byc pusty");

    checkCheckBoxes(3);
    if(formValid == 4){
      document.getElementById("thank_you").style.display = 'flex';
      document.getElementById("task-frontend").style.display = 'none';
      document.getElementById("right-panel").style.width = "100%";
      document.getElementById("right-panel").style.borderRadius = "8px";
    }

    formValid = 0;
  });

  let engine = (id, serial, message) => {
    if (id.value.trim() !== "") {
      id.style.border = "1px solid black";
      errorMsg[serial].innerHTML = "";
      formValid++;
    }else {
      errorMsg[serial].innerHTML = message;
      id.style.border = "2px solid red";
      //formValid--;
    }
  }

  let checkCheckBoxes = (serial) => {
    if (frontendCheckbox.checked == false && mobileCheckbox.checked == false && graphicsCheckbox.checked == false && backendCheckbox.checked == false){
      errorMsg[serial].innerHTML = "Musisz wybrać conjamniej jedną opcję";
    } else {
      errorMsg[serial].innerHTML = "";
      formValid++;
    }
  }