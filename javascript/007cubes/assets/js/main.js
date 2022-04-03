
function findNb(m) {
    // your code
    let rem = m, i = 0;
    while(rem > 0){
      i += 1;
      rem -= i*i*i;
    }
    return rem === 0 ? i : -1;
}
