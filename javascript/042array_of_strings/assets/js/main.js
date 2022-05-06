function arrAdder(arr) {
  let str = "";
  for(let i = 0; i < arr[0].length; i++){
    for(let j = 0; j < arr.length; j++){
      str += arr[j][i];
    }
    str+=" ";
  }
  return str.substring(0, str.length-1);
}
