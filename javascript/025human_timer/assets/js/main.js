function pad(integer){
  let g = integer%100;
  if(g < 10){
    return "0" + g;
  }
  return g
}

function humanReadable (seconds) {
  let hours = Math.floor(seconds/3600);
  let minutes = Math.floor((seconds%3600)/60);
  let secs = seconds %60;
  return pad(hours) + ':' + pad(minutes) + ':' + pad(secs);
}
