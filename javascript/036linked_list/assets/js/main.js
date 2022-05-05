class Node {
  constructor(data, next = null) {
    this.data = data;
    this.next = next;
  }
}


function parse(string) {
  if(string === "null"){
    return null;
  }
  let i = 0;
  while(string[i] !== " " || string[i+1] !== "-" || string[i+2] !== ">" || string[i+3] !== " "){
    i+=1;
  }
  return new Node(Number(string.substring(0,i)), parse(string.substring(i+4)))
}
