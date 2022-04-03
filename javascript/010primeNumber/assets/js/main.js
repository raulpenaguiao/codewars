

function isPrime(num) {
    if(num <= 1) return false;
    if(num%2 === 0) return num ===2;
    for(let i = 3; i * i <= num; i+= 2){
      if(num% i === 0) return false;
    }
    return true;
    //TODO
  }
  