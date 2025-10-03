<div align="center">
  <img src="front-end/arquivos/img/logo_keepinventory.png" alt="Logo KeepInventory" width="200">
</div>

# 📦 KeepInventory: Sistema de Gestão de Estoque de Mercado

O **KeepInventory** é um sistema moderno de gestão de inventário e produtos, focado em otimizar o controle de estoque em ambientes de varejo (mercados e lojas). O projeto demonstra o uso de **HTML, CSS (Bootstrap) e JavaScript puro** para criar uma interface de usuário eficiente e lógica de sistema robusta, incluindo autenticação e controle de promoções com prazos.

---

## Índice

- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Estrutura de Pastas](#estrutura-de-pastas)
- [Páginas e Funcionalidades](#páginas-e-funcionalidades)
- [Funcionalidades Principais](#funcionalidades-principais)
- [Acesso e Permissões (Mock)](#acesso-e-permissões-mock)
- [Como Rodar Localmente](#como-rodar-localmente)

---

## 🛠️ Tecnologias Utilizadas
![HTML](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JS](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![PYTHON](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

- **HTML5:** Estrutura e semântica das páginas.
- **CSS3:** Estilização, layout e design.
- **JavaScript:** Lógica de negócios, manipulação do DOM e interatividade.
- **Python:** Simulação da lógica do sistema se tivesse back-end.

---

## Estrutura de Pastas

A organização do projeto é focada em separar os elementos de Front-end (HTML, CSS e JS) para facilitar a manutenção e o desenvolvimento.

```
KeepInventory [GITHUB]/
├── front-end/              
│   ├── css/                
│   │   ├── global.css      
│   │   └── ...
│   ├── html/               
│   │   ├── login.html
│   │   ├── estoque-produtos.html
│   │   ├── promocao-produtos.html  
│   │   ├── fornecimento.html
│   │   ├── geral-produto.html
│   │   └── ...
│   ├── arquivos/           
│   └── js/                 
│       └── app.js          
└── README.md
```

---

## Páginas e Funcionalidades

O sistema é dividido em módulos de gestão acessíveis de acordo com o nível de permissão do usuário.

### `html/login.html` e `html/cadastro.html`
- **Descrição:** Páginas para autenticação e registro de novos colaboradores (Cadastro visível apenas para Admin/Gerente).
- **Funcionalidade:** Gerenciam o acesso ao sistema, distinguindo entre diferentes níveis hierárquicos.

### `html/estoque-produtos.html` (Gestão de Produtos)
- **Descrição:** Dashboard principal para visualização e gestão de todos os produtos em estoque.
- **Funcionalidade:** Permite adicionar, editar e remover produtos; visualização rápida do estoque atual vs. estoque mínimo.

### `html/promocao-produtos.html` (Gestão de Promoções)
- **Descrição:** Página crucial para a estratégia de vendas, onde as promoções são configuradas.
- **Funcionalidade:**
    - Ativação/Desativação de promoções por produto.
    - Definição do **Novo Preço Promocional**.
    - Configuração de **Data de Início** e **Data de Fim** para o período promocional.

### `html/fornecimento.html` (Fornecimento)
- **Descrição:** Módulo para gerenciar pedidos a fornecedores e rastreamento de entradas.
- **Funcionalidade:** Simula a requisição de produtos faltantes com base nos níveis de estoque.

### `html/geral-produto.html` (Geral Produto)
- **Descrição:** Relatórios e gráficos de visão geral sobre o inventário.
- **Funcionalidade:** Oferece *insights* sobre performance de vendas, produtos com baixo estoque e histórico de movimentação.

---

## Funcionalidades Principais

- **Autenticação e Autorização:** Controle de acesso baseado em perfis (Admin, Gerente, Estoquista).
- **Gestão de Inventário:** Manutenção completa dos dados do produto (Nome, Preço, Categoria, Localização, etc.).
- **Promoções com Prazo:** Implementação da funcionalidade de definir preço e o prazo de validade (início/fim) das ofertas.
- **Dark Mode:** Botão para alternar entre temas de cor, melhorando a ergonomia e acessibilidade.
- **Dados Simulados (`app.js`):** Uso de JavaScript para simular a persistência e manipulação de dados em tempo real no navegador.

---

## 🔑 Acesso e Permissões (Mock)

O sistema utiliza dados simulados (`app.js`). Use as credenciais abaixo para testar os diferentes perfis:

| Cargo | Email | Senha | Permissões Especiais |
| :--- | :--- | :--- | :--- |
| **Administrador** | `admin@fi.com` | `123` | Acesso total e **Cadastro de novos usuários**. |
| **Gerente** | `gerente@fi.com` | `123` | Acesso total e **Cadastro de novos usuários**. |
| **Estoquista** | `estoquista@fi.com` | `123` | Gerencia Estoque, Produtos e Fornecimento. |

---

## Como Rodar Localmente

Este é um projeto **Front-end puro**. Você só precisa de um navegador para executá-lo.

1.  **Clone o repositório:**
    ```bash
    git clone [SEU_LINK_DO_REPOSITORIO]
    ```

2.  **Navegue até a pasta e abra o arquivo:**
    Abra o arquivo `front-end/html/login.html` diretamente no seu navegador.

3.  **Acesse o Sistema:**
    Use uma das credenciais fornecidas na seção "Acesso e Permissões" para entrar e testar as funcionalidades.

---
