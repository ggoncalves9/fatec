// Função para fazer login no backend
async function login(username, password) {
    try {
        const response = await fetch('/api/auth/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                email: username,
                senha: password
            })
        });

        if (!response.ok) {
            const errorData = await response.json();
            throw new Error(errorData.erro || 'Erro no login');
        }

        const data = await response.json();
        if (data.access_token) {
            localStorage.setItem('jwt_token', data.access_token);
            localStorage.setItem('user_data', JSON.stringify(data.usuario));
            return true;
        }
        return false;
    } catch (error) {
        console.error('Erro no login:', error);
        throw error;
    }
}

// Função para verificar se está autenticado
function isAuthenticated() {
    const token = localStorage.getItem('jwt_token');
    if (!token) return false;

    // Verifica se o token está expirado
    try {
        const payload = JSON.parse(atob(token.split('.')[1]));
        if (payload.exp < Date.now() / 1000) {
            logout();
            return false;
        }
        return true;
    } catch (error) {
        return false;
    }
}

// Função para fazer logout
function logout() {
    localStorage.removeItem('jwt_token');
    localStorage.removeItem('user_data');
    window.location.href = '/login.html';
}

// Função para obter o token
function getToken() {
    return localStorage.getItem('jwt_token');
}

// Função para obter dados do usuário
function getUserData() {
    const userData = localStorage.getItem('user_data');
    return userData ? JSON.parse(userData) : null;
}

// Exporta as funções
window.Auth = {
    login,
    logout,
    isAuthenticated,
    getToken,
    getUserData
}; 