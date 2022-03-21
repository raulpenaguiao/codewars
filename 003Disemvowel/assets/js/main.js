
function isVowel(char){
    return char == 'a' || char == 'e' || char == 'i' || char == 'o' || char == 'u'
  }
  
  function disemvowel(str) {
    return Array.from(str).filter( c => ( false === isVowel(c.toLowerCase()))).join("")
  }