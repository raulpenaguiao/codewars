function removeSmallest(numbers) {
  if(numbers === []){
    return []
  }
  else{
    let min = numbers[0], minIndex = 0;
    for(let i = 1; i < numbers.length; i++){
      if(min > numbers[i]){
        min = numbers[i];
        minIndex = i;
      }
    }
    let ans = Array(0);
    for(let i = 0; i < numbers.length; i++){
      if(i !== minIndex){
        ans.push(numbers[i])
      }
    }
    return ans
  }
}
