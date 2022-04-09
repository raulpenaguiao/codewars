function getCount(str) {
  var vowelsCount = 0;
  for(let i=0; i<str.length; i++){
    if(str[i].toLowerCase() ==="a" || str[i].toLowerCase() ==="e" || str[i].toLowerCase() ==="i" || str[i].toLowerCase() ==="o" || str[i].toLowerCase() ==="u"){
      vowelsCount += 1;
    }
  }
  // enter your majic here
  
  return vowelsCount;
}
