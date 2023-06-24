import Navbar from './components/Navbar'
import Hero from './components/Hero'
import Footer from './components/Footer'
import Newsletter from './components/Newsletter'
import Analytics from './components/Analytics'

function LandingPage() {
    return (
        <div className="App">
        <Navbar/>
        <Hero/>
        <Newsletter/>
        <Analytics/>
        <Footer/>
        </div>
      );
}

export default LandingPage;