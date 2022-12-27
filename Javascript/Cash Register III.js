function checkCashRegister(price, cash, cid) {
    let change = cash * 100 - price * 100;
    let cidTotal = 0;
    console.log(change);
    for (let elem of cid) {
      cidTotal += elem[1] * 100;
    }
    if (change > cidTotal) {
      return {status: "INSUFFICIENT_FUNDS", change: []}
    } else if (change === cidTotal) {
      return {status: "CLOSED", change: cid}
    } else {
      cid = cid.reverse()
      let moneyUnits = {"ONE HUNDRED": 10000, "TWENTY":  2000, "TEN": 1000, "FIVE": 500, "ONE": 100, "QUARTER": 25, "DIME": 10, "NICKEL": 5, "PENNY": 1}
      console.log(cid)
      for (let elem of cid) {
        let holder = [elem[0]]
        elem[1] = elem[1] * 100
        while (change >= moneyUnits[elem[0]] && elem[1] > 0) {
            change -= moneyUnits[elem[0]]
            elem[1] -= moneyUnits[elem[0]]
            holder[1] += moneyUnits[elem[0]]
            
        }
      }
      if (change > 0) {
        return {status: "INSUFFICIENT_FUNDS", change: []}
      }
    }
  }
  checkCashRegister(19.5, 20, [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.1], ["QUARTER", 4.25], ["ONE", 90], ["FIVE", 55], ["TEN", 20], ["TWENTY", 60], ["ONE HUNDRED", 100]]);/*
  Currency Unit	Amount
  Penny	$0.01 (PENNY)
  Nickel	$0.05 (NICKEL)
  Dime	$0.1 (DIME)
  Quarter	$0.25 (QUARTER)
  Dollar	$1 (ONE)
  Five Dollars	$5 (FIVE)
  Ten Dollars	$10 (TEN)
  Twenty Dollars	$20 (TWENTY)
  One-hundred Dollars	$100 (ONE HUNDRED)
  */