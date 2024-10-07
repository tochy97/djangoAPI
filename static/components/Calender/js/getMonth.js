import { monthMax, makeSunday } from './constants';
import getWeek from './getWeek'; 

function getMonth(day, month, value, isLeap, year)
{
    return new Promise(function(resolve, reject) {
        const output = {
            data: [],
            year: year,
            month: month
        };
    
        const max = monthMax(month, isLeap);
        while(value > 1)
        {
            value -= 7;
        }
        
        value = makeSunday(day, value);
        day = "Sun";
        let nextWeek = getWeek(day, value, max, year, month);
        while(nextWeek && value <= max && nextWeek[0].value <= max && nextWeek.length)
        {
            value = value + 7;
            if(nextWeek.length <= 7)
                output.data.push(nextWeek);
            value = makeSunday(day, value);
            day = "Sun";
            nextWeek = getWeek(day, value, max, year, month);
        }
        
      resolve(output);
    });
}

export default getMonth;