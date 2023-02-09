import { monthMax } from './constants';
import getWeek from './getWeek'; 

function getMonth(day, month, value, isLeap)
{
    const output = {
        data: [],
        month: month
    };

    const max = monthMax(month, isLeap);
    while(value > 1)
    {
        value -= 7;
    }
    
    let nextWeek = getWeek(day, value, max)
    while(nextWeek && value < max + 7 && nextWeek[0].value < max && nextWeek.length)
    {
        value = value + 7;
        if(nextWeek.length <= 7)
            output.data.push(nextWeek);
        nextWeek = getWeek(day, value, max)
    }
    
    return output;
}

export default getMonth;