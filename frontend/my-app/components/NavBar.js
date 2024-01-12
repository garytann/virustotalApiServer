// components/Navbar.js

import Link from 'next/link';
import styles from './Navbar.module.css';

const Navbar = () => {
  return (
    <nav className={styles.navbar}>
      <div className={styles.logo}>
        <Link href="/">
          {/* Removed the <a> tag here */}
          ScanFileApp
        </Link>
      </div>
      <div className={styles.links}>
        <Link href="/about">About</Link>
        <Link href="/dashboard">
            Get Started
        </Link>
      </div>
    </nav>
  );
};

export default Navbar;
