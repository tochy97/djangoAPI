import React from 'react';
import { monthContainer, monthGrid } from '../../common/ClassNames';
import { oneYear } from '../calculation/constants';
import Days from '../Days/Days';
import WeekHeader from '../Header/WeekHeader';
import MonthHeader from '../Header/MonthHeader';

function Months( { thisMonth, year } ) {
    const month = thisMonth.info.month;
    const today = new Date();
    
    const currentMonth = (year === today.getFullYear() && oneYear[today.getMonth()] === month);
    const birthMonth = (year === 1997 && month === 'Jul');
    const gradMonth = (year === 2022 && month === 'Dec');
    return (
        <div className={monthContainer}>
            <MonthHeader month={month} year={year}/>
                <WeekHeader month={month}/>
                <div className={monthGrid}>
                {
                    thisMonth.info.data.map((element, index) => (
                        element.map((inner, innerIndex) => (
                            <Days 
                                key={`${index} ${inner?.value} ${innerIndex}`} 
                                value={inner?.value} 
                                month={month}
                                year={year}
                                status={
                                    (currentMonth && inner?.value === today.getDate()) 
                                    ? "today" 
                                    :(birthMonth && inner?.value === 28)
                                    ? "birthday"
                                    :(gradMonth && inner?.value === 21)
                                    ? "graduation"
                                    : ""
                                } 
                            />
                        ))
                    ))
                }
                </div>
        </div> 
    );
}

export default Months;