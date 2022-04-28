let check = function(num, str){//Checks if a string is made up of blocks of size num each
  if(str.length % num !== 0) return false;
  let blocks = str.length/num;
  for(let i = 0; i < blocks; i++){
    for(let j = i*num + 1; j < (i+1)*num; j++){
      if(str[j - 1] !== str[j]) return false;
    }
  }
  return true;
}


let factor = function(str){
  for(let i = str.length; i > 1; i--){
    if(check(i, str)){
      let newStr = "";
      for(let j = 0; j < str.length; j+= i){
        newStr += str[j];
      }
      return newStr;
    }
  }
  return str;
}


var decodeBits = function(bits){
    // ToDo: Accept 0's and 1's, return dots, dashes and spaces
    let dashB = /111/, dotB = /1/, spaceB = /0000000/, nexB = /0/;
    let shortBits = factor(bits);
    return shortBits.replace(/111/g, '-').replace(/1/g, '.').replace(/0000000/g, ' $ ').replace(/000/g, ' ').replace(/0/g, '');
}

let morseDecoder = function(str){
  if(str === "$") return " ";
  return MORSE_CODE[str];
}

var decodeMorse = function(morseCode){
    return morseCode.split(" ").map(morseDecoder).join("");
}
