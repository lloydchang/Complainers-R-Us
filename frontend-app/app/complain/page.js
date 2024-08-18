"use client";
import styles from '../page.module.css'; // Ensure this path is correct
import { Box, Stack, Typography, TextField, Button, Grid, IconButton } from "@mui/material";
import SendIcon from '@mui/icons-material/Send';
import * as React from 'react';
import { useState, useRef } from 'react';
import Breadcrumbs from '@mui/material/Breadcrumbs';
import Link from '@mui/material/Link';
import KeyboardVoiceIcon from '@mui/icons-material/KeyboardVoice';
import Image from 'next/image'; // Ensure correct import of Image

export default function ComplainPage() {
  const [mediaRecorder, setMediaRecorder] = useState(null);
  const [audioChunks, setAudioChunks] = useState([]);
  const [isRecording, setIsRecording] = useState(false);
  const [audioUrl, setAudioUrl] = useState(null);
  const [transcribedText, setTranscribedText] = useState('');
  const audioRef = useRef(null);

  const handleStartRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const recorder = new MediaRecorder(stream);
      setMediaRecorder(recorder);

      recorder.ondataavailable = (e) => {
        setAudioChunks((prev) => [...prev, e.data]);
    };

    recorder.start();
    setIsRecording(true);
  } catch (error) {
    console.error('Error accessing microphone:', error);
  }
};

const handleStopRecording = () => {
  if (mediaRecorder) {
    mediaRecorder.stop();
    mediaRecorder.onstop = async () => {
      const audioBlob = new Blob(audioChunks, { type: 'audio/wav; codecs=opus' });
      const url = URL.createObjectURL(audioBlob);
      setAudioUrl(url);
      setIsRecording(false);


      const formData = new FormData();
      formData.append('file', audioBlob, 'audio.wav');

    try {
        const response = await fetch('http://localhost:8000/transcribe', {
            method: 'POST',
            body: formData
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        console.log('Transcription:', data.transcribed_text);
    } catch (error) {
        console.error('Error during transcription:', error);
    }
};
    };
  };

// const handlePlayAudio = () => {
//   if (audioUrl) {
//     const audio = new Audio(audioUrl);
//     audio.play();
//   }
// }

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
      <Grid container spacing={2}>
      <Grid item xs={12} sm={8}>
      <Stack 
        direction={'column'}
        width="100%"
        height="90vh"
        p={2}
        spacing={3}
        margin="auto"
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
            className={isRecording ? styles.pulsing : ''}
            onMouseDown={handleStartRecording}
            onMouseUp={handleStopRecording}
            // onClick={handlePlayAudio}
          >
            <KeyboardVoiceIcon />
          </Button>
        </Box>
        <Stack direction={'row'} >
          <TextField
            label="Type your message here"
            fullWidth
            onChange={(e) => console.log(e.target.value)}
            InputProps={{
              endAdornment: (
                <IconButton color="primary">
              <SendIcon />
            </IconButton>
              ),
            }}
          />
        </Stack>
      </Stack>
      </Grid>
      <Grid item xs={12} sm={4}>
      <div className={styles['image-container-complain']}>
        <Image 
          src="/Complainers Я Us.jpg" 
          alt="Description" 
          width={400}
          height={400}
          objectFit="cover"
          // className={styles.image} 
        />
      </div></Grid>
      </Grid>
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
