function rangeOfNumbers(startNum, endNum) {
    //1,2
    
    if(startNum < endNum){
      rangeOfNumbers.push(startNum);
      startNum = startNum + 1;
    }else{
      return [startNum] || [endNum];
    }
    return [];
    
  };
  
  
  //endNum - startNum + 1