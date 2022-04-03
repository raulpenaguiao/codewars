var uniqueInOrder=function(iterable){
  let arr = new Array(0);
  for(let item of iterable){
    let bool = (arr.length === 0) || (item !== arr[arr.length - 1]);
    if(bool){
      arr.push(item);
    }
  }
  return arr;
}
