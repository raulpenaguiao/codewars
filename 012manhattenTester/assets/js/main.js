
function isValidWalk(walk) {
    let xCoor=0, yCoor=0, count = 0;
    function parse(char){
      count += 1;
      if(char === 's') xCoor -= 1;
      if(char === 'e') yCoor -= 1;
      if(char === 'w') yCoor += 1;
      if(char === 'n') xCoor += 1;
    }
    walk.forEach(parse);
    return (count === 10) && (xCoor === 0) && (yCoor === 0)
  }