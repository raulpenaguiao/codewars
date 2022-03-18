function toCamelCase(str){
    //console.log(str.split(/-|_/))
    /*console.log(str.split(/-|_/).map((item, index)=>{
      console.log("item = ", item, " and index = ", index)
      if(index == 0){
        return item
      } else{
        return item.replace(/^\w/, (c) => c.toUpperCase())
      }
    }).join(""))*/
    return str.split(/-|_/).map((item, index)=>{
      if(index == 0){
        return item
      } else{
        return item.replace(/^\w/, (c) => c.toUpperCase())
      }
    }).join("")
  }



  
