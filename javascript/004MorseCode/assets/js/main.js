decodeMorse = function(morseCode){
    //your code here
    let arr = morseCode.split(" ").map(x => {
      if(x === ''){
        return "SPACE"
      } else {
        return MORSE_CODE[x]
      }
    })
    let arr1 = []
    for(let i = 0; i < arr.length; i++){
      if(arr[i] === "SPACE"){
        if(i>0 && (i === arr.length - 1 || arr[i+1] !== "SPACE")){
          arr1.push(" ")
        }
      } else {
        arr1.push(arr[i])
      }
    }  
    return arr1.join("")
  }
