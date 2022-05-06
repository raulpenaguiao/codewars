function compare(str1, str2){
  let l1 = str1.length, l2 = str2.length;
  for(let i = 0; i < l1; i++){
    boolean = true;
    for(let j = 0; j < l2 && boolean; j++){
      if(str1[i] === str2[j]){
        boolean = false;
      }
    }
    if (boolean) return false;
  }
  for(let i = 0; i < l2; i++){
    boolean = true;
    for(let j = 0; j < l1 && boolean; j++){
      if(str2[i] === str1[j]){
        boolean = false;
      }
    }
    if (boolean) return false;
  }
  return true;
}

function solve(arr){
  let vis = new Array(), n = arr.length, ans = new Array();
  for(let i = 0; i < n; i++) vis.push(false);
  for(let i = 0; i < n; i++)if(!vis[i]){
    let counter = i;
    for( let j = i+1; j < n; j++)if(!vis[i] && compare(arr[i], arr[j])){
      counter += j;
      vis[j] = true;
    }
    if (counter > i){
      ans.push(counter);
    }
  }
  ans.sort((a, b) => a - b);
  return ans;
};
