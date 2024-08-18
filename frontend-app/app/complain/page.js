"use client";
import styles from '../page.module.css'; // Ensure this path is correct
import { Box, Stack, Typography, TextField, Button } from "@mui/material";
import * as React from 'react';
import Breadcrumbs from '@mui/material/Breadcrumbs';
import Link from '@mui/material/Link';
import KeyboardVoiceIcon from '@mui/icons-material/KeyboardVoice';
import Image from 'next/image'; // Ensure correct import of Image

export default function ComplainPage() {
  function handleClick(event) {
    event.preventDefault();
    console.info('You clicked a breadcrumb.');
  }

  return (
    <Box
      width="100vw"
      height="100vh"
      display="flex"
      flexDirection="column"
      justifyContent="center"
      alignItems="center"
      position="relative" // Ensure relative positioning for the container
    >
      <div role="presentation" onClick={handleClick}>
        <Breadcrumbs aria-label="breadcrumb">
          <Link underline="hover" color="inherit" href="/">
            Home
          </Link>
          <Link
            underline="hover"
            color="text.primary"
            href="/complain"
            aria-current="page"
          >
            Talk to Us
          </Link>
        </Breadcrumbs>
      </div>
      <Stack 
        direction={'column'}
        width="700px"
        height="700px"
        p={2}
        spacing={3}
      >
        <Stack 
          direction={'column'} 
          spacing={2}
          flexGrow={1}
          overflow={'auto'}
          maxHeight="100%"
        >
          <Box display={'flex'}>
            <Box
              bgcolor={'#f3e6cc'}
              borderRadius={16}
              p={3}
            >
              I am a chatbot. How can I help you today?
            </Box>
          </Box>
        </Stack>
        <Box display="flex" justifyContent="center" my={2}>
          <Button
            variant="contained"
            sx={{
              width: '60px',
              height: '60px',
              borderRadius: '50%',
              minWidth: '40px', // Ensures the button remains circular
            }}
          >
            <KeyboardVoiceIcon />
          </Button>
        </Box>
        <Stack direction={'row'} border={"solid 1px #060f12"} borderRadius={2}>
          <TextField
            label="Type your message here"
            fullWidth
            onChange={(e) => console.log(e.target.value)}
            sx={{
              '& .MuiOutlinedInput-root': {
                '& fieldset': {
                  border: 'none',
                },
              },
            }}
          />
          <Button variant="contained" color="primary">Send</Button>
        </Stack>
      </Stack>
      <div className={styles['image-container-complain']}>
        <Image 
          src="/Complainers Я Us.jpg" 
          alt="Description" 
          layout="fill"
          objectFit="cover"
          className={styles.image} 
        />
      </div>
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
    </Box>
  );
}
