// 1. odwróć liczbę
// np dla 12345, funkcja powinna zwrócić 54321
function reverseNumber(number) {
  return parseInt(number.toString().split('').reverse().join('')) * Math.sign(number);
}

let form = document.getElementById("form");
let value  = document.getElementById("value");
let result = document.getElementById("result");

form1.addEventListener("submit", (e) => {
  e.preventDefault();

  result.innerHTML = "Result = " + reverseNumber(value.value);
})




// 2. doodaj do siebie wszystkie wartości z tablicy, które są parzyste
// dla tablicy tab powinniśmy otrzymać 2 + 4 + 6 + 8 = 20
function addEven(array) {

  return array.filter(i => i%2 == 0).reduce((sum, a) => sum + a,0);
}

let form2 = document.getElementById("form2");
let value2 = document.getElementById("value2");
let result2 = document.getElementById("result2");


form2.addEventListener("submit", (e) => {
  e.preventDefault();

  let arr = value2.value.replace(/\D/g,'').split('').map(Number);
  result2.innerHTML = "Result = " + addEven(arr);
})

