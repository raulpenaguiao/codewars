function digital_root(n) {
  if(n<10){
    return n;
  } else{
    let sum_digs = 0, pow10 = 10, num = n;
    while(num > 0){
      sum_digs += num % 10;
      num = Math.floor(num/10);
    }
    return digital_root(sum_digs)
  }
  // ...
}
