function parseLetter(letter){
  if(letter == "M"){
    return 1000;
  }
  if(letter == "D"){
    return 500;
  }
  if(letter == "C"){
    return 100;
  }
  if(letter == "L"){
    return 50;
  }
  if(letter == "X"){
    return 10;
  }
  if(letter == "V"){
    return 5;
  }
  if(letter == "I"){
    return 1;
  }
}

function solution (roman) {
  let arr = roman.split("").map(parseLetter);
  arr2 = [];
  for(let i = 1; i< arr.length; i++){
    if(arr[i] <= arr[i-1]){
      arr2.push(arr[i-1]);
    } else{
      arr[i] =  arr[i] - arr[i-1];
    }
  }
  arr2.push(arr[arr.length - 1]);
  return arr2.reduce((a, b) => a+b);
  
  // complete the solution by transforming the 
  // string roman numeral into an integer
  return 0;
}
