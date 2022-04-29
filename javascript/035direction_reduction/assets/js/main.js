const N = "NORTH", S = "SOUTH", E = "EAST", W = "WEST";

function opposite(str){
  if(str === N) return S;
  if(str === S) return N;
  if(str === E) return W;
  if(str === W) return E;
}

function oneRed(arr){
  for(let i = 1; i < arr.length; i++){
    if(arr[i] === opposite(arr[i-1])){
      let narr = new Array();
      for(let j = 0; j < arr.length; j++){
        if(j !== i && j !== i-1){
          narr.push(arr[j])
        }
      }
      return narr;
    }
  }
  return arr;
}

function dirReduc(arr){
  let nArr = oneRed(arr);
  if (arr === nArr) return arr;
  return dirReduc(nArr);
  // ...
}
