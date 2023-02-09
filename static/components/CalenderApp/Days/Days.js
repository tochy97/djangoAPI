import React from 'react';
import { MdToday } from 'react-icons/md';
import { FaBirthdayCake, FaGraduationCap } from 'react-icons/fa';
import Modal from '../../common/Modal/Modal';
import { calenderIcons, dayContainer, modalContentContainer, modalHeaderContainer, modalIcons } from '../../common/ClassNames';

function Days({ value, month, year, status }) {
  
  return (
    <>
      {
        value !== 0 ?
          <Modal 
            trigger={
              <div className={dayContainer}>
                {value} 
                {(status === "today") && <div className={calenderIcons}><MdToday/></div>}
                {(status === "birthday") && <div className={calenderIcons}><FaBirthdayCake/></div>}
                {(status === "graduation") && <div className={calenderIcons}><FaGraduationCap/></div>}
              </div>
            } 
            header={
              <div className={modalHeaderContainer}>
                <div className='mr-3'>{month} {value}, {year}</div>
                {(status === "today") && <div className={modalIcons}><MdToday/></div>}
                {(status === "birthday") && <div className={`mt-1 ${modalIcons}`}><FaBirthdayCake/></div>}
                {(status === "graduation") && <div className={modalIcons}><FaGraduationCap/></div>}
              </div>
            } 
            content={
              <div className={modalContentContainer}></div>
            }
            fullScreen={true}
          />
        :
        <div className="md:h-24"/>
      }
    </>
  );
}

export default Days;