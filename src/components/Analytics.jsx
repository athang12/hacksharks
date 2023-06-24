import React from 'react';

import Lottie from 'lottie-react'
import pl from '../media/pl.json'

const Analytics = () => {
  return (
    <div className='bg-[url("./1.jpeg")]'>
    <div className='flex flex-row'>
    <div>
      <Lottie animationData={pl} className='ml-60 w-96 h-96 border-white  '/>
      </div>
      <div className='text-white text-8xl text-center border-white  w-1/2 pr-24 pt-20'>
        Discover<br></br>Yourself !
      </div>

    </div>
    <div className='w-full bg-white py-16 px-4 text-white  flex flex-row text-center bg-[url("./1.jpeg")]'>
      <div className='w-1/3 ml-16 border-white border-2'>
        <h2 className='text-3xl font-bold'>Customised</h2>
        <p className='text-2xl'>bvisubv<br></br>wsdvar<br></br>crev</p>
      </div>

      <div className='w-1/3 border-white border-2'>
        <h2 className='text-3xl font-bold'>Easy to access</h2>
      </div>

      <div className='w-1/3 border-white border-2 mr-16'>
      <h2 className='text-3xl font-bold'>Feature title</h2>
      </div>
    </div>
    </div>
  );
};

export default Analytics;
