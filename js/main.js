const input = document.querySelector('.chat-user-input');
const sendBtn = document.querySelector('.chat-send-btn');
const messages = document.querySelector('.chat-messages');

function sendMessage() {
    const text = input.value.trim();
    if (text === '') return;

    // Create a new message div
    const msgDiv = document.createElement('div');
    msgDiv.classList.add('chat-message'); // for styling later
    msgDiv.textContent = text;

    // Append to messages container
    messages.appendChild(msgDiv);

    // Clear input and focus again
    input.value = '';
    input.focus();

    // Scroll to the latest message
    messages.scrollTop = messages.scrollHeight;
}

// Send on button click
sendBtn.addEventListener('click', sendMessage);

// Send on Enter key
input.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        e.preventDefault();
        sendMessage();
    }
});
