function findEvenIndex(arr){
  let tot = arr.reduce((a, c) => a+c);
  let acc = 0;
  for(let i = 0; i < arr.length; i++){
    if(acc*2 === tot - arr[i]) return i;
    acc += arr[i];
  }
  return -1;
  //Code goes here!
}
