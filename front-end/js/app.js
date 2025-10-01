const CARGOS_PERMITIDOS_CADASTRO = ['admin', 'gerente', 'tecnico_ti'];
const CARGOS_PERMITIDOS_PRODUTOS = ['admin', 'gerente', 'estoquista', 'comprador', 'caixa', 'auditor'];

const USUARIOS = [
    { id: 101, email: 'admin@fi.com', senha: '123', nome: 'Administrador', tipo_conta: 'admin' },
    { id: 102, email: 'gerente@fi.com', senha: '123', nome: 'Gerente de Operações', tipo_conta: 'gerente' },
    { id: 103, email: 'estoquista@fi.com', senha: '123', nome: 'João Estoquista', tipo_conta: 'estoquista' },
    { id: 105, email: 'caixa@fi.com', senha: '123', nome: 'Pedro Caixa', tipo_conta: 'caixa' },
    { id: 106, email: 'auditor@fi.com', senha: '123', nome: 'Ana Auditora', tipo_conta: 'auditor' },
    { id: 107, email: 'ti@fi.com', senha: '123', nome: 'Técnico de TI', tipo_conta: 'tecnico_ti' },
    { id: 108, email: 'financeiro@fi.com', senha: '123', nome: 'Carlos Financeiro', tipo_conta: 'financeiro' },
];

let PRODUTOS = [
    { id: '001', nome: 'Parafuso Philips 10mm', preco: 1.50, estoque: 500, estoque_min: 100, categoria: 'Fixadores', marca: 'FixaTudo', localizacao: 'A1-01', promocao: false, unidade: 'pc' },
    { id: '002', nome: 'Chave de Fenda Média', preco: 15.00, estoque: 85, estoque_min: 50, categoria: 'Ferramentas Manuais', marca: 'Profix', localizacao: 'B2-10', promocao: true, unidade: 'un' },
    { id: '003', nome: 'Luva de Raspa Tamanho G', preco: 25.00, estoque: 150, estoque_min: 200, categoria: 'EPIs', marca: 'SafetyMax', localizacao: 'C3-05', promocao: false, unidade: 'par' },
    { id: '004', nome: 'Tinta Acrílica Branca 3.6L', preco: 120.00, estoque: 30, estoque_min: 40, categoria: 'Tintas', marca: 'Colorsul', localizacao: 'A1-05', promocao: false, unidade: 'lt' },
    { id: '005', nome: 'Fita Isolante 10m', preco: 5.50, estoque: 300, estoque_min: 150, categoria: 'Elétrica', marca: 'Eletro+', localizacao: 'B2-01', promocao: true, unidade: 'un' },
    { id: '006', nome: 'Cimento CP II 50kg', preco: 35.00, estoque: 40, estoque_min: 100, categoria: 'Construção', marca: 'MegaCem', localizacao: 'C3-15', promocao: false, unidade: 'sc' },
    { id: '007', nome: 'Serra Copo 50mm', preco: 45.00, estoque: 15, estoque_min: 10, categoria: 'Ferramentas Elétricas', marca: 'PowerDrill', localizacao: 'A1-02', promocao: false, unidade: 'un' },
];

let MOVIMENTACOES = [
    { id: 1, tipo: 'ENTRADA', produto_id: '003', quantidade: 50, data: '2025-09-25 10:30' },
    { id: 2, tipo: 'SAIDA', produto_id: '001', quantidade: 10, data: '2025-09-25 14:00' },
    { id: 3, tipo: 'ENTRADA', produto_id: '006', quantidade: 20, data: '2025-09-26 08:00' },
    { id: 4, tipo: 'SAIDA', produto_id: '002', quantidade: 5, data: '2025-09-27 11:30' },
    { id: 5, tipo: 'ENTRADA', produto_id: '007', quantidade: 5, data: '2025-09-27 16:45' },
];


function getUsuarioLogado() {
    try {
        const usuarioJson = sessionStorage.getItem('usuarioLogado');
        return usuarioJson ? JSON.parse(usuarioJson) : null;
    } catch (error) {
        console.error("Erro ao obter usuário logado:", error);
        return null;
    }
}

function fazerLogin(email, senha) {
    const usuario = USUARIOS.find(u => u.email === email && u.senha === senha);
    if (usuario) {
        sessionStorage.setItem('usuarioLogado', JSON.stringify(usuario));
        return usuario;
    }
    return null;
}

function fazerLogout() {
    sessionStorage.removeItem('usuarioLogado');
    window.location.href = 'login.html';
}

function verificarAutorizacao(cargosPermitidos = CARGOS_PERMITIDOS_PRODUTOS) {
    const usuario = getUsuarioLogado();

    if (!usuario) {
        if (!window.location.pathname.includes('login.html')) {
            fazerLogout();
        }
        return false;
    }
    
    if (!cargosPermitidos.includes(usuario.tipo_conta)) {
        console.warn(`Usuário ${usuario.email} (${usuario.tipo_conta}) não tem permissão para acessar esta página.`);
        exibirMensagemModal("Acesso Negado", `Seu perfil (${usuario.tipo_conta}) não tem permissão para esta área.`, 'alert-danger');
        
        setTimeout(() => {
             window.location.href = 'estoque-produtos.html'; 
        }, 3000); 
        return false;
    }
    return true;
}


function buscarProdutos() {
    return [...PRODUTOS]; 
}

function buscarMovimentacoes() {
    return [...MOVIMENTACOES].sort((a, b) => new Date(b.data) - new Date(a.data));
}

function buscarProdutoPorId(id) {
    return PRODUTOS.find(p => p.id === id);
}

function getNomeProduto(id) {
    const produto = buscarProdutoPorId(id);
    return produto ? produto.nome : 'Produto Desconhecido';
}

function adicionarProduto(novoProduto) {
    const novoIdNum = PRODUTOS.length + 1;
    const novoId = 'P' + novoIdNum.toString().padStart(3, '0');
    
    const produtoCompleto = { ...novoProduto, id: novoId };
    PRODUTOS.push(produtoCompleto);
    
    console.log(`Produto adicionado: ${novoId}`);
    return novoId;
}

function atualizarProduto(id, dadosAtualizados) {
    const index = PRODUTOS.findIndex(p => p.id === id);
    
    if (index !== -1) {
        PRODUTOS[index] = { ...PRODUTOS[index], ...dadosAtualizados };
        console.log(`Produto atualizado: ${id}`);
        return true;
    }
    return false;
}

function removerProduto(id) {
    const tamanhoOriginal = PRODUTOS.length;
    PRODUTOS = PRODUTOS.filter(p => p.id !== id);
    
    if (PRODUTOS.length < tamanhoOriginal) {
        console.log(`Produto removido: ${id}`);
        return true;
    }
    return false;
}


function exibirMensagemModal(titulo, mensagem, tipo = 'alert-info') {
    if (typeof bootstrap === 'undefined') {
        console.error("Bootstrap não carregado. Exibindo alerta simples:", mensagem);
        alert(`${titulo}: ${mensagem}`);
        return;
    }
    
    let modalElement = document.getElementById('customAlertModal');

    if (!modalElement) {
        console.error("Elemento Modal de Alerta não encontrado (customAlertModal).");
        return;
    }

    const modalTitle = modalElement.querySelector('.modal-title');
    const modalBodyAlert = modalElement.querySelector('#customAlertMessage');

    modalTitle.textContent = titulo;
    modalBodyAlert.className = `alert ${tipo} mb-0`;
    modalBodyAlert.innerHTML = mensagem; 

    const modal = new bootstrap.Modal(modalElement);
    modal.show();
}


function atualizarIconeTema(isDarkMode) {
    const btnTema = document.getElementById('btn-toggle-darkmode');
    if (btnTema) {
        if (isDarkMode) {
            btnTema.innerHTML = '<i class="bi bi-sun"></i> Tema';
        } else {
            btnTema.innerHTML = '<i class="bi bi-moon-stars"></i> Tema';
        }
    }
}

function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    const isDarkMode = document.body.classList.contains('dark-mode');
    localStorage.setItem('darkMode', isDarkMode ? 'enabled' : 'disabled');
    
    atualizarIconeTema(isDarkMode);

    const darkModeLink = document.getElementById('dark-mode-style');
    if (isDarkMode) {
        if (!darkModeLink) {
            const link = document.createElement('link');
            link.id = 'dark-mode-style';
            link.rel = 'stylesheet';
            link.href = '../css/dark-mode.css';
            document.head.appendChild(link);
        }
    } else {
        if (darkModeLink) {
            darkModeLink.remove();
        }
    }
}


document.addEventListener('DOMContentLoaded', () => {
    if (!window.location.pathname.includes('login.html')) {
        const usuario = getUsuarioLogado();
        const navCadastro = document.getElementById('nav-cadastro');
        
        if (navCadastro) {
            if (usuario && CARGOS_PERMITIDOS_CADASTRO.includes(usuario.tipo_conta)) {
                navCadastro.style.display = 'block';
            } else {
                 navCadastro.style.display = 'none';
            }
        }
    }

    const isDarkModeEnabled = localStorage.getItem('darkMode') === 'enabled';
    if (isDarkModeEnabled && !document.body.classList.contains('dark-mode')) {
        const link = document.createElement('link');
        link.id = 'dark-mode-style';
        link.rel = 'stylesheet';
        link.href = '../css/dark-mode.css';
        document.head.appendChild(link);
        
        document.body.classList.add('dark-mode');
    }
    
    atualizarIconeTema(isDarkModeEnabled); 
});