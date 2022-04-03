function rowSumOddNumbers(n) {
    let oddNumber = 1;
      for(let i = 1; i<=n; i++){
      let count = 0;
      for(let j = 1; j <= i; j++){
        count += oddNumber;
        oddNumber += 2;
      }
      if(i === n ) return count;
    }
  }