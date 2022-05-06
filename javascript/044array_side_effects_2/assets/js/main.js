function removeNthElement(arr, n) {
  // Fix it
  var arrCopy = new Array();
  for(let i = 0; i < arr.length; i++){
    arrCopy.push(arr[i])
  }
  arrCopy.splice(n, 1); // removes the nth element
  return arrCopy;
}
