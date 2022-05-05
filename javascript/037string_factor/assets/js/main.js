function check(i, len, str){
  if(len%i !== 0) return false;
  console.log(i, str)
  boolean = true;
  let j = i;
  while(boolean && j < len){
    boolean = ( str[j%i] === str[j] );
    j += 1;
  }
  return boolean;
}

function f(s) {
  let l = s.length;
  let i = 1;
  while(!check(i, l, s)){
    i++;
  }
  return [s.substring(0,i), l/i];
  // your code here
}
