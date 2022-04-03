
function duplicateEncode(word){
    let n = word.length;
    let arr = new Array(n);
    for(let i = 0; i <n ; i++) arr[i] = 0;
    for(let i = 0; i < n; i++){
      for(let j = 0; j < n; j++){
        if(i != j && word[i].toLowerCase() === word[j].toLowerCase()) arr[i] = 1;
      }
    }
    let str = "";
    for(let i=0; i<n; i++){
      if(arr[i] === 0) str += "(";
      if(arr[i] === 1) str += ")";
    }
    return str
  }
  