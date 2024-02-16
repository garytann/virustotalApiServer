"use client";
import Image from "next/image"
import Link from 'next/link';
import { useState } from 'react';
import Logo from '@/public/next.svg'
import { AiOutlineMenu, AiOutlineClose } from 'react-icons/ai'

const Navbar = () => {

  const [menuOpen, setMenuOpen] = useState(false)

  const handleNav = () => {
    setMenuOpen(!menuOpen);
  }

  return (
    <>
    {/* -> fix on top of the screen
    w-full -> width full
    h-24 -> height 24
    shadow-xl -> shadow extra large
    bg-white -> background white */}
    <nav className="w-full h-24 shadow-xl bg-white">
      {/* flex -> flex display
      justify between -> justify content space between
      item-center -> align item center
      height full -> height full
      2xl:px-16 -> padding 16px on 2xl screen */}
      <div className="flex justify-between items-center h-full w-full px-4 2xl:px-16">
        {/* Logo */}
        {/* Logo variable is imported from the public folder */}
        <Link href="/">
          {/* <Image
            src={Logo}
            alt="Logo"
            width="205"
            height="75"
            className="cursor-pointer"
            priority
          /> */}
          <h1 className="uppercase text-xl italic">
            LOGO
          </h1>
        </Link>

        {/* Item List */}
        <div className="hidden sm:flex">
          <ul className="hidden sm:flex">
            <Link href="/about" className="w-[100%] px-2 py-2 mt-3 text-center">
              <li className="uppercase hover:border-b text-l whitespace-nowrap"> About Us</li>
            </Link>

            <Link href="/contact" className="w-[100%] px-2 py-2 mt-3 text-center">
              <li className="uppercase hover:border-b text-l"> Contact</li>
            </Link>

            <Link href="/dashboard" className="w-full px-5 py-4 mt-2 text-center text-white bg-indigo-600 rounded-md lg:ml-5">
              <li className="uppercase hover:border-b text-l whitespace-nowrap"> Get Started</li>
            </Link>
          </ul>
        </div>

        {/* Hamburger Menu */}
        {/* <div onClick={handleNav} className="sm:hidden cursor-pointer pl-24">
          <AiOutlineMenu size={25} />
        </div>

      </div>
      <div className={
        menuOpen
          ? "fixed left-0 top-0 w-[65%] sm:hidden h-screen bg-[#ecf0f3] p-10 ease-in duration-500"
          : "fied left-[-100%] top-0 p-10 ease-in duration-500"
      }
      > */}
        {/* <div className="flex w-full items-center justify-end">
          <div onClick={handleNav} className="cursor-pointer">
            <AiOutlineClose size={25} />
          </div>
        </div> */}
      </div>
    </nav>
    </>
  );
};

export default Navbar;
