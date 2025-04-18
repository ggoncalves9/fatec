// DOM Elements
const chatContainer = document.getElementById('chat-container');
const chatForm = document.getElementById('chat-form');
const userInput = document.getElementById('user-input');
const rankingBtn = document.getElementById('ranking-btn');
const rankingModal = document.getElementById('ranking-modal');
const closeRankingBtn = document.getElementById('close-ranking');
const rankingList = document.getElementById('ranking-list');
const pontuacaoElement = document.getElementById('pontuacao');

// Function to add a message to the chat
function addMessage(content, isUser = false) {
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${isUser ? 'user-message' : 'coruja-message'}`;
    
    if (typeof content === 'string') {
        messageDiv.textContent = content;
    } else {
        messageDiv.appendChild(content);
    }
    
    chatContainer.appendChild(messageDiv);
    chatContainer.scrollTop = chatContainer.scrollHeight;
}

// Function to create options grid
function createOptionsGrid(options) {
    const gridDiv = document.createElement('div');
    gridDiv.className = 'options-grid';
    
    options.forEach(option => {
        const button = document.createElement('button');
        button.className = 'option-button';
        button.textContent = option;
        button.onclick = () => {
            userInput.value = option;
            chatForm.dispatchEvent(new Event('submit'));
        };
        gridDiv.appendChild(button);
    });
    
    return gridDiv;
}

// Function to make API requests
async function makeRequest(endpoint, data = {}) {
    try {
        const response = await fetch(`/api/${endpoint}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        return await response.json();
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}

// Function to load rankings
async function loadRankings() {
    try {
        const response = await fetch('/api/ranking');
        const data = await response.json();
        
        rankingList.innerHTML = '';
        data.forEach((item, index) => {
            const rankingItem = document.createElement('div');
            rankingItem.className = 'flex justify-between items-center p-2 bg-gray-50 rounded';
            rankingItem.innerHTML = `
                <span class="font-semibold">${index + 1}. ${item.nome}</span>
                <span>${item.pontos} pontos</span>
            `;
            rankingList.appendChild(rankingItem);
        });
    } catch (error) {
        console.error('Error loading rankings:', error);
    }
}

// Function to initialize session
async function iniciarSessao() {
    try {
        const response = await makeRequest('iniciar-sessao');
        if (response.mensagem) {
            addMessage(response.mensagem);
            if (response.opcoes && response.opcoes.length > 0) {
                addMessage(createOptionsGrid(response.opcoes));
            }
        }
        if (response.pontos !== undefined) {
            pontuacaoElement.textContent = `Pontos: ${response.pontos}`;
        }
    } catch (error) {
        console.error('Error initializing session:', error);
        addMessage('Erro ao iniciar sessão. Por favor, tente novamente.');
    }
}

// Event Listeners
chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const userMessage = userInput.value.trim();
    
    if (!userMessage) return;
    
    addMessage(userMessage, true);
    userInput.value = '';
    
    try {
        const response = await makeRequest('resposta', { resposta: userMessage });
        
        if (response.mensagem) {
            addMessage(response.mensagem);
            if (response.opcoes && response.opcoes.length > 0) {
                addMessage(createOptionsGrid(response.opcoes));
            }
        }
        
        if (response.pontos !== undefined) {
            pontuacaoElement.textContent = `Pontos: ${response.pontos}`;
        }
    } catch (error) {
        console.error('Error sending message:', error);
        addMessage('Erro ao processar sua mensagem. Por favor, tente novamente.');
    }
});

rankingBtn.addEventListener('click', () => {
    rankingModal.classList.remove('hidden');
    loadRankings();
});

closeRankingBtn.addEventListener('click', () => {
    rankingModal.classList.add('hidden');
});

// Initialize session when page loads
iniciarSessao();
