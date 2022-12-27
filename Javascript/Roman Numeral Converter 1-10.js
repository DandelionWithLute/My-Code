function convertToRoman(num) {
    let romanNumeral = "";

    while (num > 0) {
        if (num < 4) {
            romanNumeral += "I";
            num -= 1
        } else if (num === 4) {
            romanNumeral += "IV";
            num -= 4;
        } else if (num === 5) {
            romanNumeral += "V";
            num -= 5;
        } else if (num === 6){
            romanNumeral += "VI";
            num -= 6;
        } else if (num === 7){
            romanNumeral += "VII";
            num -= 7;
        } else if (num === 8){
            romanNumeral += "VIII";
            num -= 8;
        } else if (num === 9) {
            romanNumeral += "IX";
            num -= 9;
        } else if (num === 10){
            romanNumeral += "X";
            num -= 10;
        } else {
            return false;
        }
    }
    return romanNumeral;
}
console.log(convertToRoman(10));