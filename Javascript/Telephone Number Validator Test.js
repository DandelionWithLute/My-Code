function telephoneCheck(str) {
    let polishNum = str.replace(/\D/g, "");
    console.log(polishNum);
    if (polishNum.length == 10) {
      let a = str.length - 2;
      if(str[a] == "-"){
        return false;
      } else {
        return true;
      }
    } else if (polishNum.length === 11 && (polishNum[0] === 1 || str[0] === 1)) {
      return true;
    } else {
      return false;
    }
    
}

console.log(telephoneCheck("1 555-555-5555")); 