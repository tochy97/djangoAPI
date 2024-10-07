import { nextDay, nextMonth } from "./constants";

function getNextMonth( thisMonth ) {
    let output = {
        month : nextMonth(thisMonth.month),
        day: "",
        value: 0
    }
    const week = thisMonth.data[thisMonth.data.length - 1]
    if(week[week.length - 1].value !== 0){
        output.value = 1;
        output.day = nextDay(week[week.length - 1].day);
    }
    else{
        let index = week.length - 1;
        while(index >= 0){
            if(week[index].value !== 0){
                output.value = 1;
                output.day = nextDay(week[index].day);
                break;
            }
            index--;
        }
    }
    return output;
}

export default getNextMonth;