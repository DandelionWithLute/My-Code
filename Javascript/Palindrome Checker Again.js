function palindrome(str) {
    sep = str.replace(/\W+|_/g, "").toLowerCase();
    rev = sep.split("").reverse().join("");
    return (sep == rev) ? true : false;
  }
  
  let result = palindrome("eyde");
  console.log(result);