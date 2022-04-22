function digitize(n) {
  if(n === 0) return [0]
  let N = n;
  let arr = new Array(0);
  while(N >0){
    arr.push(N%10);
    N = Math.floor(N/10);
  }
  return arr;
  //code here
}
