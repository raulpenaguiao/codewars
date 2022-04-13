const capitalizeFirstLetter = s => 
  s.split(' ').map(w => w.charAt(0).toUpperCase() + w.slice(1)).join(' ')
function generateHashtag (str) {
  let text = str.split(" ").map(capitalizeFirstLetter)
  text.unshift("#")
  let ans = text.join("")
  if(ans.length > 140 || ans === "#"){
    return false
  }
  return ans
}
