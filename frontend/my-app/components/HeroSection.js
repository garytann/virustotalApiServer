// components/HeroSection.js
'use client';
import Container from './Container';
import Link from 'next/link';


const HeroSection = () => {
  return (
    <>
      <Container className="flex flex-wrap ">
        <div className="flex items-center w-full lg:w-[50%]">
          <div className='max-w-2xl mb-8'>
            <h1 className='text-4xl font-bold leading-snug tracking-tight text-gray-800 lg:text-4xl lg:leading-tight xl:text-6xl xl:leading-tight dark:text-black'>
              Scan your files
            </h1>
            <p className="py-5 text-xl leading-normal text-gray-500 lg:text-xl xl:text-2xl dark:text-gray-300">
              An application that uses VirusTotal API to detect malware in your files
            </p>

            <div className="flex flex-col items-start space-y-3 sm:space-x-4 sm:space-y-0 sm:items-center sm:flex-row">

            <Link href = "/dashboard"
                className="px-8 py-4 text-lg font-medium text-center text-white bg-indigo-600 rounded-md ">
                Get Started For Free
              </Link>
              
            </div>
          </div>
        </div>
      </Container>
    </>
  );
};

export default HeroSection;
