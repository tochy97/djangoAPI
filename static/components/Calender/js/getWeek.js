import { oneWeek } from "./constants";

function getWeek(day, value, max, year, month)
{
    return new Promise(function(resolve, reject) {
        const weekDiv = document.createElement("div");
        if(value <= -7)
        {
            return null;
        }

        const output = []
        const today = day;

        const nextsunday = value + 7;
        let index = 0;
        while(value < 1)
        {
            value++;
            index++;
            output.push(
                {
                    value: 0
                }
            )
        }
        day = oneWeek[index]
        const dayDiv = document.createElement("div");
        output.push(
            {
                year: year,
                month: month,
                day: day,
                value: value
            }
        )
        weekDiv.innerHTML = dayDiv;
        weekDiv.setAttribute('start', year + month + value);

        let weekIndex;
        while((value < nextsunday - 1 ) && (max > 0 && value < max))
        {
            dayDiv = document.createElement("div");
            weekIndex = oneWeek.indexOf(day);
            day = oneWeek[weekIndex + 1];
            value++;
            output.push(
                {
                    year: year,
                    month: month,
                    day: day,
                    value: value
                }
            )
        }
        while(output.length < 7)
        {
            output.push(
                {
                    value: 0
                }
            )
        }
        resolve(output);
    });
}

export default getWeek;