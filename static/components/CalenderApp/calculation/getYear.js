import getMonth from "./getMonth";
import getNextMonth from "./getNextMonth";
import getPrevMonth from "./getPrevMonth";

function getYear(today, isLeap, year, isNow) {
    let day = today.split(' ')[0];
    let month = today.split(' ')[1];
    let value = parseInt(today.split(' ')[2]);
    const thisMonth = getMonth(day,month,value, isLeap);

    const output = [
        {
            year: year,
            month: month,
            status: (isNow ? "thisMonth" : ""),
            thisMonth: isNow ? true : false,
            myBirthday: year === 1997 && month === "Jul" ? true : false,
            myGraduation: year === 2022 && month === "Dec" ? true : false,
            info: thisMonth
        }
    ];
    
    let next = getNextMonth(thisMonth, isLeap);
    let nextMonth = getMonth(next.day, next.month, next.value, isLeap);
    
    if(month !== "Dec"){
        while(next.month !== "Dec"){
    if(year === 1997){
        console.log(year, month)
    }
            output.push(
                {
                    year: year,
                    month: next.month,
                    status: "",
                    thisMonth: isNow ? true : false,
                    myBirthday: year === 1997 && next.month === "Jul" ? true : false,
                    myGraduation: year === 2022 && next.month === "Dec" ? true : false,
                    info: nextMonth
                }
            );
            
            next = getNextMonth(nextMonth, isLeap);
            nextMonth = getMonth(next.day, next.month, next.value, isLeap);
        }

    if(year === 1997){
        console.log(year, month)
    }
        output.push(
            {
                year: year,
                month: next.month,
                status: "",
                thisMonth: isNow ? true : false,
                myBirthday: year === 1997 && next.month === "Jul" ? true : false,
                myGraduation: year === 2022 && next.month === "Dec" ? true : false,
                info: nextMonth
            }
        );
    }

    let prev = getPrevMonth(thisMonth, isLeap);
    let prevMonth = getMonth(prev.day, prev.month, prev.value, isLeap);
    if(month !== "Jan")
    {
        while(prev.month !== "Jan"){
            output.unshift(
                {
                    year: year,
                    month: prev.month,
                    status: "",
                    thisMonth: isNow ? true : false,
                    myBirthday: year === 1997 && prev.month === "Jul" ? true : false,
                    myGraduation: year === 2022 && prev.month === "Dec" ? true : false,
                    info: prevMonth
                }
            );

            prev = getPrevMonth(prevMonth, isLeap);
            prevMonth = getMonth(prev.day, prev.month, prev.value, isLeap);
        }
        
        output.unshift(
            {
                year: year,
                month: prev.month,
                status: "",
                thisMonth: isNow ? true : false,
                myBirthday: year === 1997 && prev.month === "Jul" ? true : false,
                myGraduation: year === 2022 && prev.month === "Dec" ? true : false,
                info: prevMonth
            }
        );
    }
    return output;
}

export default getYear;