import React from 'react';
import { weekContainer, weekHeaderContainer } from '../../common/ClassNames';
import { oneWeek } from '../calculation/constants';

function WeekHeader() {

    return (
        <div className={weekHeaderContainer}>
        {
            oneWeek.map((element, index) => (
                <div className={weekContainer} key={index}>
                    {element}
                </div>
            ))
        }
        </div>
    );
}

export default WeekHeader;