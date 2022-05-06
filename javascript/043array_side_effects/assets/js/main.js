function withoutLast(arr) {
  let ans = new Array();
  for(let i = 0; i < arr.length - 1; i++){
    ans.push(arr[i]);
  }
  // Fix it
  //arr.pop(); // removes the last element
  return ans;
}
