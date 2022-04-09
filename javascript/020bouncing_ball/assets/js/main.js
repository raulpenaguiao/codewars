function bouncingBall(h,  bounce,  window) {
  if(h <= 0 || 0 >= bounce || bounce >= 1 || window >= h){
    return -1
  }
  let count = 1;
  let heigth = h * bounce;
  while(heigth > window){
    heigth *= bounce;
    count += 2;
  }
  return count;
  // your code here
}
