
function pos(item, arr, occurs){
  let counter = 0;
  let n = arr.length;
  for(let i=0; i<n; i++){
    if(arr[i] === item){
      if (counter === occurs) return i;
      counter += 1;
    }
  }
}


function sortArrays(arr1,arr2){
  //console.log("inputs = ", arr1, arr2)
  let sArr1 = new Array(), sArr2 = new Array(), n = arr1.length;
  for(let i = 0; i < n; i++){
    sArr1.push(Number(arr1[i]));
    sArr2.push(Number(arr2[i]));
  }
  sArr1.sort();
  sArr2.sort();
  console.log("sorteds = ", sArr1, sArr2)
  let pArr1 = new Array(), pArr2 = new Array();
  for(let i=0; i<n; i++){
    let occs1 = 0, occs2 = 0;
    for(let j = 0; j < i; j++){
      if(sArr1[i]===sArr1[j]) occs1+= 1;
      if(sArr2[i]===sArr2[j]) occs2+= 1;
    }
    pArr1.push(pos(sArr1[i], arr1, occs1));
    pArr2.push(pos(sArr2[i], arr2, occs2));
  }
  //console.log("positions = ", pArr1, pArr2)
  let ansArr1 = new Array(), ansArr2 = new Array();
  for(let i=0; i<n; i++){
    ansArr1.push(Number(arr1[pArr2[i]]));
    ansArr2.push(Number(arr2[pArr1[i]]));
  }
  console.log("ans = ", ansArr1, ansArr2)
  return [ansArr1, ansArr2];
}

