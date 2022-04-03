function solution(str){
  if(str.length%2 === 1) str+="_";
  let lis = new Array(0);
  for(i = 0; i< str.length; i+=2){
    lis.push(str[i] + str[i+1])
  }
  return lis
}
