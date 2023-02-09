import React from 'react';
import { monthHeader } from '../../common/ClassNames';

function MonthHeader( { month, year } ) {
    return (
        <div className={monthHeader}>
            <p>{year}</p>
            <p>{month}</p>
        </div>
    );
}

export default MonthHeader;