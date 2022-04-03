function highAndLow(numbers){
  let arr = numbers.split(" ").map(x => Number(x)).sort((x, y) => x - y);
  console.log(arr)
  return arr[arr.length - 1] + " " + arr[0];
}
