function rot(strng) {
  let arr = strng.split("\n");
  let n = arr.length;
  let ans = new Array();
  for(let i = n-1; i >= 0; i--){
    let st = "";
    for(let j=n-1; j>= 0; j--){
      st+=arr[i][j];
    }
    ans.push(st);
  }
  let ter = ans.join("\n")
  return ans.join("\n");
}
function selfieAndRot(strng) {
  let arr = strng.split("\n");
  let n = arr.length;
  let ans = new Array();
  let dots = "";
  for(let i = 0; i < n; i++){
    let st = "";
    dots += ".";
    for(let j=0; j<n ; j++){
      st+=arr[n-i-1][n-j-1];
    }
    ans.push(st);
  }
  arr = arr.map(str => str + dots);
  ans = ans.map(str => dots + str);
  return arr.join("\n") + "\n" +  ans.join("\n");
}
function oper(fct, s) {
    return fct(s);
}
