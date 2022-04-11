function validatePIN (pin) {
  l = pin.length;
  if(l !== 4 && l !== 6){
    return false;
  }
  for(let i=0; i<l; i++){
    if (pin[i] < '0' || pin[i] > '9') {
      return false;
    }
  }
  return true
}
