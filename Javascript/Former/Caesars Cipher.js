function rot13(str){
    let result = "";
    let strA = "ABCDEFGHIJKLM"
    let strB = "NOPQRSTUVWXYZ"
    for (let i = 0; i < str.length; i++){
        let a = strA.indexOf(str[i]);//Not strB[i]
        let b = strB.indexOf(str[i]);//Not strA[i]
        if (a >= 0) {//Don't forget the chance of circumstance is equal to 0
            result += strB[a];
        } else if (b >= 0){
            result += strA[b];//result += strA[i] If you want to bind i in B with A,then you should write strA[str.indexOf(strB[i])]
        } else {
            result += str[i];
        }
        
    }
    return result;
}

console.log(rot13("FREE CODE CAMP"));
