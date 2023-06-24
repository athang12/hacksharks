<div className='bg-black'>
        <Parallax pages={3} ref={ref}>
        <ParallaxLayer offset={0}  style={
          {
            backgroundImage:`url(${a})`,
            backgroundSize:`100% 100%`
          }
        } >
        </ParallaxLayer>
  
        <ParallaxLayer offset={1} style={
          {
            backgroundImage:`url(${b})`,
            backgroundSize:`100% 100%`
          }
        } >
        
        </ParallaxLayer>
        <ParallaxLayer sticky={{start:0.3,end:1.5}} speed={1} className=''>
          <img src={as} className='w-60 h-60 border-white ml-96'/>
        </ParallaxLayer>
        <ParallaxLayer offset={0} factor={2} speed={0.5}>
          <h1 className='text-8xl text-blue-500 text-center ml-96 mt-96 border-white  '>Welcome to <br></br>
          our site <br></br>lets get started !</h1>
        </ParallaxLayer>
        <ParallaxLayer offset={1} factor={2
        } speed={0.5}>
          <h1 className='text-8xl text-blue-500 text-center ml-96 mt-96 border-white  '>hii</h1>
        </ParallaxLayer>
      </Parallax>
      </div>