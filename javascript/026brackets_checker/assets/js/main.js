function validBraces(braces){
  if(braces === ""){
    return true;
  }
  console.log("Evaluating ", braces);
  for(let i=0; i + 1< braces.length; i++){
    if(  (braces[i] === "(" && braces[i+1] === ")") || (braces[i] === "[" && braces[i+1] === "]") || (braces[i] === "{" && braces[i+1] === "}") ){
      let str = braces.substring(0, i) + braces.substring(i+2, braces.length);
      return validBraces(str);
    }
  }
  return false;
}
