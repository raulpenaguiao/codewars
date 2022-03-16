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