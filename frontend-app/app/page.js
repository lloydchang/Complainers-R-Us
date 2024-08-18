"use client"
import styles from "./page.module.css";
import { Button, Typography } from "@mui/material";
import { useTheme } from '@mui/material/styles';
import Spline from '@splinetool/react-spline';
// import { useRouter } from "next/router";
// import { useEffect } from "react";



export default function Home() {
  // const router = useRouter();
  // useEffect(() => {
  //   router.push("/complain");
  // }, []);
  const theme = useTheme();

  return (
    <main className={styles.main}>
      <Typography variant="h1" component="h1" sx={{ fontFamily: 'TAN Headline' }} gutterBottom>
        Complainers <span style={{ transform: 'scaleX(-1)', display: 'inline-block', color: theme.palette.primary.main }}>R</span> Us
      </Typography>
      {/* <Spline
        scene="https://prod.spline.design/bzCBgayWPlzmJn71/scene.splinecode" 
        width={922}
        height={593}
      /> */}
      <Button variant="contained" color="primary" href="/complain"> Complain </Button>
    </main>
  );
}
