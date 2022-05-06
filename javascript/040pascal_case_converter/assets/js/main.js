function toLower(str){
  let newStr = "";
  for(let i = 0; i < str.length; i++){
    newStr += str[i].toLowerCase();
  }
  return newStr;
}

function splitting(arr, list){
  if(list.length === 0) {
    return arr;
  }
  let ans = new Array(), l = new Array();
  arr.forEach(str => {
    ans = ans.concat(str.split(list[0]));
    return str
  });
  for(let i=1; i<list.length; i++){
    l.push(list[i]);
  }
  return splitting(ans, l)
}

function capit(str){
  if (str === "") return "";
  return str[0].toUpperCase() + toLower(str.substring(1))
}

function camelize(str){
  console.log(str)
  let arr = splitting([str], ["'", '"', "=", ">", "<", "+", ",", "-", " ", "/", ":", "_", ";", "?", "!", "."]);
  arr = arr.map(capit);
  return arr.join("")
}
