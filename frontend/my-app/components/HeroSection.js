// components/HeroSection.js

import styles from './Herosection.module.css';
import Link from 'next/link';

const HeroSection = () => {
  return (
    <div className={styles.hero}>
      <div className={styles.content}>
        <div className={styles.text}>
          <h1 className={styles.title}>Upload Files</h1>
          <Link href="/dashboard">
            <button className={styles.button}>
              Get Started
            </button>
          </Link>
        </div>
        <div className={styles.image}>
          <img src="/site_design_2.jpg" priority />
        </div>
      </div>


    </div>
  );
};

export default HeroSection;
