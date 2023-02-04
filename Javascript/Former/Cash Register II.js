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