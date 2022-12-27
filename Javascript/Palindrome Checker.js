function palindrome(str) {
    let polishedString = str.replace(/\W+|_/g, "").toLowerCase();
    let reverseString = polishedString.split("").reverse().join("");

    return (polishedString == reverseString) ? true : false;
}
    let result = palindrome("eye")
    console.log(result)