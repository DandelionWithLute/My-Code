function telephoneCheck(str) {
    if (str.indexOf("(") === -1 && str.indexOf(")") > -1) return false;
      let polishNum = str.replace(/-| /g, "");
      if (polishNum.length == 10) {
        return true;
      } else if (polishNum.length === 11 && str[0] === 1) {
        return true;
      } else {
        return false;
      }
    }
    
    telephoneCheck("555-555-5555");