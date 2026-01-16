const input = document.querySelector('.chat-user-input');
const sendBtn = document.querySelector('.chat-send-btn');
const messages = document.querySelector('.chat-messages');

async function sendMessage() {
    try {
    const question = input.value.trim();
    console.log("Sending question:", question);
    if (!question) return;

    // Show user message in chat
    const userMsg = document.createElement('div');
    userMsg.classList.add('chat-message', 'user');
    userMsg.textContent = question;
    messages.appendChild(userMsg);

    input.value = ''; // clear input
    input.focus();

    // Send request to backend
    const res = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question })
    });
    console.log("FETCH STATUS:", res.status);
    const text = await res.text();
    console.log("Backend response:", text);
    // 5️⃣ Parse JSON
    const data = JSON.parse(text);
    console.log("PARSED DATA:", data);

    // Show bot response
    const botMsg = document.createElement('div');
    botMsg.classList.add('chat-message', 'bot');
    botMsg.textContent = data.response;
    console.log(
        "BOT TEXT =",
        botMsg.textContent,
        botMsg.textContent.length
    );
    messages.appendChild(botMsg);

    // Scroll to latest message
    messages.scrollTop = messages.scrollHeight;
    } catch (err) {
        console.error("JS ERROR:", err);
    }
}

// Trigger send on button click
sendBtn.addEventListener('click', sendMessage);

// Trigger send on Enter key
input.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        e.preventDefault();
        sendMessage();
    }
});

