import { monthMax, prevDay, prevMonth } from './constants';

function getPrevMonth(thisMonth, isLeap) {
    let output = {
        month : prevMonth(thisMonth.month),
        day: "",
        value: 0
    }
    const week = thisMonth.data[0];
    if(week[0].value !== 0){
        output.value = monthMax(output.month, isLeap);
        output.day = prevDay(week[0].day);
    }
    else{
        let index = 0;
        while(index <= week.length - 1){
            if(week[index].value !== 0){
                output.value = monthMax(output.month, isLeap);
                output.day = prevDay(week[index].day);
                break;
            }
            index++;
        }
    }
    return output;
}

export default getPrevMonth;