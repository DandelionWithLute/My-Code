/*
PROJ 1

function factorialize(num) {
    let product = 1;
    for (let i = 2; i <= num; i++) {
      product *= i;
    }
    return product;
  }
  
console.log(factorialize(5));
*/

/*
PROJ 2q
function factorialize(num) {
    if(num === 0){
        return 1;
    }else{
        return num * factorialize(num - 1);
    }
  }
  
  console.log(factorialize(5));

  */



  function factorialize(num, factorial = 1) {
    if(num === 0){
        return factorial;
    }else{
        return factorialize(num - 1, num * factorial)
    }
  return num;
}

console.log(factorialize(5));