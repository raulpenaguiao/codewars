function max(arr){
  let m = arr[0];
  for(let i=1; i<arr.length; i++){
    if(m < arr[i]){
      m = arr[i]
    }
  }
  return m;
}

function min(arr){
  let m = arr[0];
  for(let i=1; i<arr.length; i++){
    if(m > arr[i]){
      m = arr[i]
    }
  }
  return m
}

function minMax(arr){
  return [min(arr), max(arr)]; // fix me!
}
