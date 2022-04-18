function productFib(prod){
  let fibbsa = 0, fibbsb = 1, fibbsc, pr = 0;
  while(pr < prod){
    fibbsc = fibbsa + fibbsb;
    fibbsa = fibbsb;
    fibbsb = fibbsc;
    pr = fibbsa*fibbsb;
  }
  if(pr === prod){
    return [fibbsa, fibbsb, true];
  } else{
    return [fibbsa, fibbsb, false];
  }
  // ...
}
