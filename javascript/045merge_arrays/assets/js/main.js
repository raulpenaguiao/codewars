function mergeArrays(a, b) {
  let la = a.length, lb = b.length;
  let ans = new Array();
  let m = Math.min(la, lb);
  for(let i = 0; i < m; i++){
    ans.push(a[i]);
    ans.push(b[i]);
  }
  if(la < lb){
    for(let i = m; i < lb; i++){
      ans.push(b[i]);
    }
  }else{
    for(let i = m; i < la; i++){
      ans.push(a[i]);
    }
  }
  return ans;
  // your code here
}
