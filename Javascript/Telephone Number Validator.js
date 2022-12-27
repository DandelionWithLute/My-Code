function telephoneCheck(str) {
    
        let polishNum = str.replace(/\D/g, "");
        console.log(polishNum);
        
        if (str.indexOf(/\?\w/g) > 0){
            return false;
          }
        if (str.indexOf("(") >= 0 && str.indexOf(")") < 0 || str.indexOf(")") >= 0 && str.indexOf("(") < 0){
          return false;
        }
        if (str[0] == "(" && str[str.length - 1] == ")"){
          return false;
        }
        if (str[0] == "-"){return false;}
        if (str.indexOf("?") >= 0){return false;}
        if (str[str.length -2 ] == "-"){return false;}
        if (polishNum.length == 10) {
          return true;
        } else if (polishNum.length === 11) {
            console.log(polishNum[0])
            return (polishNum[0] == 1 ? true : false);
        } else {
          return false;
        }
    }
    
    console.log(telephoneCheck("1 456 789 4444")); 