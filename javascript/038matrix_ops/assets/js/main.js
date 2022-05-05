function rot90Clock(strng) {
  let arr = strng.split("\n");
  let n = arr.length;
  let ans = new Array();
  for(let i = 0; i < n; i++){
    let st = "";
    for(let j=n-1; j>= 0; j--){
      st+=arr[j][i];
    }
    ans.push(st);
  }
  let ter = ans.join("\n")
  return ans.join("\n");
}
function diag1Sym(strng) {
  let arr = strng.split("\n");
  let n = arr.length;
  let ans = new Array();
  for(let i = 0; i < n; i++){
    let st = "";
    for(let j=0; j<n ; j++){
      st+=arr[j][i];
    }
    ans.push(st);
  }
  return ans.join("\n");
}
function selfieAndDiag1(strng) {
  let arr = strng.split("\n");
  let n = arr.length;
  let ans = new Array();
  for(let i = 0; i < n; i++){
    let st = "";
    for(let j=0; j<n ; j++){
      st+=arr[j][i];
    }
    ans.push(arr[i]+ "|" + st);
  }
  return ans.join("\n");
  return strng;
    // your code
}
function oper(fct, s) {
  return fct(s);
    // your code
}
