import { oneWeek } from "./constants";

function getWeek(day, value, max)
{
    if(value <= -7)
    {
        return null;
    }

    const output = []
    const today = day;
    switch(day)
    {
        case "Mon":
            value -= 1;
            day = "Sun";
            break;
        case "Tue":
            value -= 2;
            day = "Sun";
            break;
        case "Wed":
            value -= 3;
            day = "Sun";
            break;
        case "Thu":
            value -= 4;
            day = "Sun";
            break;
        case "Fri":
            value -= 5;
            day = "Sun";
            break;
        case "Sat":
            value -= 6;
            day = "Sun";
            break;
        default:
            break;
    }

    const nextsunday = value + 7;
    let index = 0;
    while(value < 1)
    {
        value++;
        index++;
        output.push(
            {
            day: "",
            value: 0
        })
    }
    day = oneWeek[index]
    output.push(
        {
        day: day,
        value: value
    })

    let weekIndex;
    while((value < nextsunday - 1 ) && (max > 0 && value < max))
    {
        weekIndex = oneWeek.indexOf(day);
        day = oneWeek[weekIndex + 1];
        value++;
        output.push(
            {
            day: day,
            value: value
        })
    }
    while(output.length < 7)
    {
        output.push(
            {
            day: "",
            value: 0
        })
    }
    return output;
}

export default getWeek;