import { isLeap, monthMax, prevDay } from './constants';
import getYear from "./getYear";

function getPast(endYear) {
    const today = new Date();
    const stringDay = (today).toString();
    const thisYear = getYear(stringDay, isLeap(today.getFullYear()), today.getFullYear(), true);
    let year = new Date().getFullYear();
    let leap = isLeap(year);

    const output = 
    [
        {
            year: year,
            data: thisYear,
            status: "thisYear",
            leap: leap
        },
    ]

    year--;
    leap = isLeap(year);
    let startDay = prevDay(thisYear[0].info.data[0].filter(element => element.value !== 0)[0].day);
    const startMonth = "Dec";
    const startValue = monthMax(startMonth);
    let lastYear = getYear(startDay +  " " + startMonth + " "  + startValue, leap, year, false);

    while(year >= endYear)
    {
        output.unshift(
            {
                year: year,
                data: lastYear,
                status: (year === 1997 ? "myBirthday" : year === 2022 ? "myGraduation" : ""),
                leap: leap
            }
        );
        year--;
        leap = isLeap(year);
        startDay = prevDay(lastYear[0].info.data[0].filter(element => element.value !== 0)[0].day);
        lastYear = getYear(startDay +  " " + startMonth + " "  + startValue, leap, year, false);
    }debugger
    return output;
}

export default getPast;