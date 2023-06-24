import React, { useState } from 'react';
import { motion } from 'framer-motion';
import BM from './data/BM';
import HM from './data/HM';
import ST from './data/ST.js';
import SSH from './data/SSH';

import scienceData from './science';
import technologyData from './technology';
import sportsData from './sports';
import booksData from './books';
import hobbiesData from './hobbies';

import { BrowserRouter as Router,useNavigate, Switch, Route, Redirect, Link , useLocation} from 'react-router-dom';
import axios from "axios"
import Lottie from "lottie-react"
import ab from './media/ab.json'
import d from './media/d.json'
import down from './media/down.json'
import { Parallax, ParallaxLayer } from '@react-spring/parallax'
import {useRef, useEffect} from "react";
import a from './media/1.jpeg' 
import b from './media/2.jpg'
import as from'./media/as.gif'


const InterestsPage = () => {
  
  const location=useLocation()
  // const email = " "
  const email=location.state.id
  
  const [selectedCheckboxes, setSelectedCheckboxes] = useState([]);

  const handleCheckboxChange = (checkboxName) => {
    setSelectedCheckboxes((prevSelectedCheckboxes) => {
      if (prevSelectedCheckboxes.includes(checkboxName)) {
        // Checkbox is already selected, remove it from the array
        return prevSelectedCheckboxes.filter((checkbox) => checkbox !== checkboxName);
      } else {
        // Checkbox is not selected, add it to the array
        return [...prevSelectedCheckboxes, checkboxName];
      }
    });
  };

    const history=useNavigate()
    const [expandedSections, setExpandedSections] = useState([]);
    const si=[]
    const ob=[]
  
    const handleShowMore = (sectionId) => {
      setExpandedSections((prevExpandedSections) => [...prevExpandedSections, sectionId]);
    };
  
    const handleShowLess = (sectionId) => {
      setExpandedSections((prevExpandedSections) =>
        prevExpandedSections.filter((id) => id !== sectionId)
      );
    };
    
    const smsl=true
    const isSectionExpanded = (sectionId) => expandedSections.includes(sectionId);
  
    const handleImageClick = (name,isSelected) => {
        // console.log(isSelected)
        
        var result = ob.find(item => item.name === name);
        if(result)
        {
            if(result.sel)
            {
                result.sel=false
            }
            else
            {
                result.sel=true
            }
        }
        else
        {
            ob.push({
                "name":name,
                "sel":!isSelected
            })
            // si.push(name)
        }
        console.log(ob)
        // console.log(result)
        // console.log(si)
        isSelected=!isSelected
      };
      
  
      const [isImageBlurred, setIsImageBlurred] = useState(false);

    async function handleSubmit(e){
      // Perform submit action here

    //   for(const item of ob)
    //   {
    //     if(item.sel===true)
    //     {
    //         si.push(item.name)
    //     }
    //   }
    //   console.log(si)

    console.log(selectedCheckboxes);
    // const si = []
    
      e.preventDefault();
      try{

          await axios.post("http://localhost:3000/interests",{
              selectedCheckboxes,email
          })
          .then(
        
                  history("/thankyou",)
             
          )
          .catch(e=>{
              alert("wrong info")
              console.log(e);
          })

      }
      catch(e){
          console.log(e);

      }

    };
  

    const [selectedImages, setSelectedImages] = useState([]);

    const handleClick = (name) => {
      setSelectedImages((prevSelectedImages) => {
        if (prevSelectedImages.includes(name)) {
          // If the image is already selected, remove it from the array
          return prevSelectedImages.filter((image) => image !== name);
        } else {
          // If the image is not selected, add it to the array
          return [...prevSelectedImages, name];
        }
      });
    };


  
    const interests = [
      {
        id: 1,
        name: 'Science and Technology',
        data: ST,
      },
      {
        id: 2,
        name: 'Health and Medicine',
        data: HM,
      },
      {
        id: 3,
        name: 'Social Sciences and Humanities',
        data: SSH,
      },
      {
        id: 4,
        name: 'Business and Management',
        data: BM,
      },
    ];
  
    

    const ref = useRef()



    return (
      <div className='bg-[url("./1.jpeg")]'>
        


      <div offset={3} className='border-white border-2 bg-[url("./1.jpeg")]'>
      <div className="bg-[url('./1.jpeg')]  text-white min-h-screen flex flex-col items-center justify-center">
      <div className='flex flex-row'>
        <h1 className="text-4xl font-bold font-montserrat mb-8 pt-16">Interests</h1>
        <Lottie animationData={d} className='w-24 h-24 border-white  mt-8'/>
        </div>
  
        {interests.map((interest) => {
          const { id, name, data } = interest;
          const isExpanded = isSectionExpanded(name);
  
          return (
            <div
              key={id}
              className={`w-full max-w-7xl mx-4 my-8 ${
                isExpanded ? 'bg-gray-800' : 'bg-gray-800'
              } rounded-lg px-8 py-6`}
            >
              <h2 className="text-3xl font-bold mb-4">{name}</h2>
  
              <div className="flex flex-wrap justify-between">
                {data.slice(0, isExpanded ? data.length : 5).map((item) => {
                  const { id, name, image ,isSelected} = item;
                  const imageId = `image-${id}`;
    
  
                  return (
                    <motion.div
                      key={id}
                      className="relative w-1/5 h-1/5 my-2 cursor-pointer"
                      whileHover={{ scale: 1.1 }}
                      
                    >
                    
                    <label>
                    <input
                      type="checkbox"
                      checked={selectedCheckboxes.includes(name)}
                      onChange={() => handleCheckboxChange(name)}
                    />
                    <img src={image} alt={name} className='w-44 h-44'/>
                  </label>
                      <h3 className='text-center'>{name}</h3>
  
                      {isSelected && (
                        <div className="absolute top-0 left-0 right-0 bottom-0 bg-black bg-opacity-50 flex items-center justify-center">
                          <svg
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="white"
                            className="h-6 w-6"
                          >
                            <path
                              strokeLinecap="round"
                              strokeLinejoin="round"
                              strokeWidth={2}
                              d="M5 13l4 4L19 7"
                            />
                          </svg>
                        </div>
                      )}
                    </motion.div>
                  );
                })}
              </div>
  
              {data.length > 5 && (
                <div className="flex justify-center">
                  <button
                    className="bg-black text-white text-2xl rounded w-60 mt-8"
                    onClick={() => (isExpanded ? handleShowLess(name) : handleShowMore(name))}
                  >
                  <div className='flex felx-row '>
                    <div className='border-white  pt-4 ml-4 w-60'>{isExpanded ? 'Show Less' : 'Show More'}</div>
                    {smsl ? <Lottie animationData={down} className='w-32 h-20 border-white '/>: 'by'}
                    </div>
                  </button>
                </div>
              )}
            </div>
          );
        })}
  
        <Lottie animationData={ab} className="w-24 h-24 border-2 border-white"/>
        <button className="mt-8 bg-black text-white rounded px-4 py-2 border-2 border-white mb-4" onClick={handleSubmit}>
          Submit
        </button>

      </div>
      </div>


      

      </div>
    );
  };
  
  export default InterestsPage;