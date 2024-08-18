"use client";
import styles from '../page.module.css'; 
import { Box, Stack, Typography, TextField, Button, Grid, IconButton } from "@mui/material";
import SendIcon from '@mui/icons-material/Send';
import * as React from 'react';
import { useState, useRef, useEffect } from 'react';
import Breadcrumbs from '@mui/material/Breadcrumbs';
import Link from '@mui/material/Link';
import KeyboardVoiceIcon from '@mui/icons-material/KeyboardVoice';
import Image from 'next/image'; 
import ChatComponent from '../components/Chat'; 

export default function ComplainPage() {
  const [mediaRecorder, setMediaRecorder] = useState(null);
  const [audioChunks, setAudioChunks] = useState([]);
  const [isRecording, setIsRecording] = useState(false);
  const [audioUrl, setAudioUrl] = useState(null);
  const [transcribedText, setTranscribedText] = useState('');
  const audioRef = useRef(null);
  const [messages, setMessages] = useState([]);
    const [message, setMessage] = useState('');
    const messagesEndRef = useRef(null);

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

const handleSendMessage = async () => {
  if (message.trim()) {
      const newUserMessage = { text: message, sender: 'user' };
      setMessages(prevMessages => [...prevMessages, newUserMessage]);
      setMessage('');

      try {
          // const botResponse = await getMessageResponse(message);
          const botResponse = 'I am a chatbot. How can I help you today?';
          const newBotMessage = { text: botResponse, sender: 'venie' };
          setMessages(prevMessages => [...prevMessages, newBotMessage]);
      } catch (error) {
          console.error('Failed to get bot response:', error);
          const errorMessage = { text: "Sorry, I couldn't process your request. Please try again later.", sender: 'venie' };
          setMessages(prevMessages => [...prevMessages, errorMessage]);
      }
  }
};

const handleKeyDown = (e) => {
  if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSendMessage();
  }
};

useEffect(() => {
  // Automatically scroll to the bottom when a new message is added
  if (messagesEndRef.current) {
      messagesEndRef.current.scrollIntoView({ behavior: "smooth" });
  }
}, [messages]);

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
  height="calc(100vh - 100px)" // Adjust height to account for top and bottom margins
  p={2}
  spacing={3}
  margin="16px 0" // 16px margin on top and bottom, 0 on left and right
>
        {/* <Stack 
          direction={'column'} 
          spacing={2}
          flexGrow={1}
          overflow={'auto'}
          maxHeight="100%"
        >
          <Box className={styles.chatbox__messages}>
                        <Box
                            className={`${styles.messages__item} ${styles.messages__item_operator}`}
                        >
                            How can I help you today?
                        </Box>
                    {messages.map((msg, index) => (
                        <Box
                            key={index}
                            className={`${styles.messages__item} ${msg.sender === 'venie' ? styles.messages__item_operator : styles.messages__item_visitor}`}
                        >
                            {msg.text}
                        </Box>
                    ))}
                    <div ref={messagesEndRef} />
                </Box>
        </Stack> */}
        <ChatComponent messages={messages} />
        <Box display="flex" justifyContent="center" my={2}>
          <Button
            variant="contained"
            sx={{
              width: '60px',
              height: '60px',
              borderRadius: '50%',
              minWidth: '40px', // Ensures the button remains circular
            }}
            className={`${styles.button} ${isRecording ? styles.pulsing : ''}`}
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
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            onKeyDown={handleKeyDown}
            InputProps={{
              endAdornment: (
                <IconButton className={`${styles.chatbox__send__footer} ${styles.send__button}`}
                onClick={handleSendMessage}>
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
