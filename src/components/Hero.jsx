import React from 'react';
import Typed from 'react-typed';
import a from '../media/1.jpeg'
import Lottie from 'lottie-react'
import mail from '../media/mail.json'

const Hero = () => {
  return (
    <div className="text-white flex flex-row bg-[url('./1.jpeg')]">     <div className='max-w-[800px] mt-[-96px] w-2/3 h-screen mx-auto text-center flex flex-col justify-center border-white'>
        <p className='text-[#00df9a] font-bold p-2'>
          LEARN AND GROW
        </p>
        <h1 className='md:text-6xl sm:text-6xl text-4xl font-bold md:py-6'>
        Empower Your Mind with Curated Research Papers
        </h1>
        <div className='flex justify-center items-center'>
          <p className='md:text-4xl sm:text-4xl text-xl font-bold py-4'>
            Get papers on : <br></br>
          </p>
          <Typed
          className='md:text-4xl sm:text-4xl text-xl font-bold md:pl-4 pl-2'
            strings={['Science and Technology','Social Sciences','Health and Medicine','Business and Management']}
            typeSpeed={120}
            backSpeed={140}
            loop
          />
        </div>
        <p className='md:text-2xl text-xl font-bold text-gray-500'>Get the papers from all over the web best suited for you</p>
        <button className='bg-[#00df9a] w-[200px] rounded-md font-medium my-6 mx-auto py-3 text-black'>Get Started</button>
      </div>
      <div className='w-1/3 p-20 mt-4'>
        <Lottie animationData={mail}/>
      </div>
    </div>
  );
};

export default Hero;
