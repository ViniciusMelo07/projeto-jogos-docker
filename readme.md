# 🎮 Catálogo de Jogos — Projeto Flask + Front-End

Este projeto é uma aplicação simples de CRUD para gerenciamento de jogos, com:

- Backend em **Flask + SQLite**
- Frontend em **HTML, CSS e JavaScript**
- Contêineres separados via **Docker Compose**

---

## 🚀 Como rodar o projeto com Docker Compose

### 🧱 Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

---

### 📁 Estrutura do projeto

projeto/
│
├── backend/
│ ├── app.py
│ ├── routes.py
│ ├── database.py
│ ├── requirements.txt
│ └── Dockerfile
│
├── frontend/
│ ├── index.html
│ ├── style.css
│ ├── script.js
│ └── Dockerfile
│
└── docker-compose.yml

### ▶️ Passo a passo para rodar

1. **Clone o repositório** ou baixe o ZIP
2. No terminal, vá até a pasta do projeto
3. Rode os seguintes comandos:

```bash
docker-compose down -v --remove-orphans
docker-compose build --no-cache
docker-compose up

🌐 Acessos
Frontend: http://localhost:8080

Backend/API: http://localhost:5000/games

O front consome a API via http://backend:5000 pela rede interna do Docker.