function solution(str, ending){
  return ending === str.substring(str.length - ending.length, str.length)
}
