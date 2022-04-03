function mostFrequentDays(year){
    let weekDays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    let date = new Date(Date.UTC(year, 0, 1));
    let firstWeekDay = date.toLocaleDateString('en-US', {
      weekday: 'long',
    })
    //console.log("for year = ", year, " we get ", firstWeekDay)
    if( year % 4 != 0 || ( year%100 == 0 && year%400 != 0 ) ){
      return  [firstWeekDay]
    } else{
      let nextWeekDay, i=0
      while(weekDays[i] != firstWeekDay){
        i++
      }
      nextWeekDay = weekDays[(i+1)%7]
      if(nextWeekDay == "Monday"){
        return [nextWeekDay, firstWeekDay]
      } else{
       return [firstWeekDay, nextWeekDay] 
      }
    }
  }


const btn = document.querySelector("p");
const form_year = document.querySelector("input");
const ans = document.querySelector("h2")


btn.addEventListener('click', () => {
  let year = parseInt(form_year.value)
  if(isNaN(year) || typeof year === "undefined"){
    ans.innerHTML = "Invalid value"
  } else{
    let arr = mostFrequentDays(year)
    ans.innerHTML = arr[0]
    if(arr.length == 2){
      ans.innerHTML += " and "
      ans.innerHTML += arr[1]
    }
  }
})