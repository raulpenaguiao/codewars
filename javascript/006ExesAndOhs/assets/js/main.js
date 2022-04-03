
function XO(str) {
    //code here
    let countx = 0, counto = 0;
    for(let i = 0; i < str.length; i++){
      if(str[i] == "x" || str[i] == "X") countx+=1;
      if(str[i] == "o" || str[i] == "O") counto+=1;
    }
    return countx === counto
  }