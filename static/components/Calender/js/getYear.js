import getMonth from "./getMonth";
import getNextMonth from "./getNextMonth";
import getPrevMonth from "./getPrevMonth";

function getYear(today, isLeap, year, isNow) {
    return new Promise(async function(resolve, reject) {
        let day = today.split(' ')[0];
        let month = today.split(' ')[1];
        let value = parseInt(today.split(' ')[2]);
        const thisMonth = await getMonth(day,month,value, isLeap, year);
        const output = [
            {
                year: year,
                month: month,
                thisMonth: (isNow ? true : false),
                myGraduation: year === 2022 && month === "Dec" ? true : false,
                info: thisMonth
            }
        ];
        
        let next = getNextMonth(thisMonth, isLeap);
        let nextMonth = await getMonth(next.day, next.month, next.value, isLeap, year);
        
        if(month !== "Dec"){
            while(next.month !== "Dec"){
                output.push(
                    {
                        year: year,
                        month: next.month,
                        thisMonth: false,
                        myBirthday: year === 1997 && next.month === "Jul" ? true : false,
                        myGraduation: year === 2022 && next.month === "Dec" ? true : false,
                        joinMiliary: year === 2020 && month === "Jan" ? true : false,
                        info: nextMonth
                    }
                );
                
                next = getNextMonth(nextMonth, isLeap);
                nextMonth = await getMonth(next.day, next.month, next.value, isLeap, year);
            }
            output.push(
                {
                    year: year,
                    month: next.month,
                    thisMonth: false,
                    myGraduation: year === 2022 && next.month === "Dec" ? true : false,
                    info: nextMonth
                }
            );
        }
    
        let prev = getPrevMonth(thisMonth, isLeap);
        let prevMonth = await getMonth(prev.day, prev.month, prev.value, isLeap, year);
        if(month !== "Jan")
        {
            while(prev.month !== "Jan"){
                output.unshift(
                    {
                        year: year,
                        month: prev.month,
                        thisMonth: false,
                        myBirthday: year === 1997 && prev.month === "Jul" ? true : false,
                        joinMiliary: year === 2020 && prev.month === "Jan" ? true : false,
                        info: prevMonth
                    }
                );
    
                prev = getPrevMonth(prevMonth, isLeap);
                prevMonth = await getMonth(prev.day, prev.month, prev.value, isLeap, year);
            }
            
            output.unshift(
                {
                    year: year,
                    month: prev.month,
                    thisMonth: false,
                    myBirthday: year === 1997 && prev.month === "Jul" ? true : false,
                    joinMiliary: year === 2020 && prev.month === "Jan" ? true : false,
                    info: prevMonth
                }
            );
        }
        resolve(output);
    });
}

export default getYear;