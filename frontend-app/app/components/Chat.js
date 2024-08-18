import React, { useRef, useEffect } from 'react';
import { Box, Button, Stack } from '@mui/material';
import styles from './chat.module.css'; // Adjust the import according to your project structure

const ChatComponent = ({ messages }) => {
  const messagesEndRef = useRef(null);

  useEffect(() => {
    if (messagesEndRef.current) {
      messagesEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [messages]);

  return (
    <Stack
    direction={'column'} 
          spacing={2}
          flexGrow={1}
          overflow={'auto'}
          maxHeight="100%">
      <Box className={styles.chatbox__messages}>
        <Box className={`${styles.messages__item} ${styles.messages__item_operator}`}>
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
    </Stack>
  );
};

export default ChatComponent;