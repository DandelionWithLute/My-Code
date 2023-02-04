function rot13(str) {
    let strA = 'ABCDEFGHIJKLM'
    let strB = 'NOPQRSTUVWXYZ'
    let arr = ""

    for (let i = 0; i < str.length; i++){
        let j = str.indexOf(strA) || str.indexOf(strB);
            if (str[j] in strA){
                arr += strB[j]
            } else if (str[j] in strB){
                arr += strA[j]
            } else {
                arr += " ";
            }
        }
        return arr;
    }
    
  
  
console.log(rot13("SERR PBQR PNZC"));