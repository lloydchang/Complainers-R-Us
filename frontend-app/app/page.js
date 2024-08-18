"use client";
import styles from './page.module.css'; // Ensure this path is correct
import { Button, Typography, Stack } from "@mui/material";
import { useTheme } from '@mui/material/styles';
import Link from 'next/link';
import Image from 'next/image';
import { useRouter } from 'next/navigation';

export default function Home() {
  const theme = useTheme();
  const router = useRouter();

  const handleNavigation = () => {
    router.push('/complain');
  };

  return (
    <Stack
  className={styles.main}
  direction="column"
  spacing={2} // Adjust the spacing value as needed
  sx={{ height: '100vh', width: '100vw' }} // Full height and width
>
      {/* <Typography variant="h1" component="h1" sx={{ fontFamily: 'TAN Headline' }} gutterBottom>
        Complainers <span style={{ transform: 'scaleX(-1)', display: 'inline-block', color: theme.palette.primary.main }}>R</span> Us
      </Typography> */}
      <div className={styles['image-container-home']}>
        <Image 
          src="/Complainers Я Us.jpg" 
          alt="Description" 
          layout="fill"
          objectFit="cover"
          className={styles.image} 
        />
      </div>
      <Button className={styles.button} variant="contained" onClick={handleNavigation}> 
        Let's Complain 
      </Button>
      
      <footer className={styles.footer}>
        <Link
          href="https://github.com/Complainers-R-Us/Complainers-R-Us"
          target="_blank"
          rel="noopener noreferrer"
          style={{ textDecoration: 'none', color: 'inherit' }} // Optional styling for link
        >
          <Typography variant="body1">© 2024 Complainers Я Us</Typography>
        </Link>
      </footer>
    </Stack>
  );
}
