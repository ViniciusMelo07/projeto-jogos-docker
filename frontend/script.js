const api = 'http://localhost:5000';

document.querySelector('#addGameForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const nome = document.querySelector('#nome').value;
  const categoria = document.querySelector('#categoria').value;
  const ano = document.querySelector('#ano').value;

  const res = await fetch(`${api}/games`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ nome, categoria, ano })
  });

  const msg = await res.json();
  document.querySelector('#mensagem').textContent = msg.mensagem || 'Erro ao adicionar.';
  e.target.reset();
  carregarJogos();
});

document.querySelector('#updateGameForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const id = document.querySelector('#id_update').value;
  const nome = document.querySelector('#nome_update').value;
  const categoria = document.querySelector('#categoria_update').value;
  const ano = document.querySelector('#ano_update').value;

  const res = await fetch(`${api}/update`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ id, nome, categoria, ano })
  });

  const msg = await res.json();
  document.querySelector('#mensagem').textContent = msg.mensagem || msg.erro;
  e.target.reset();
  carregarJogos();
});

document.querySelector('#deleteGameForm').addEventListener('submit', async (e) => {
  e.preventDefault();
  const id = document.querySelector('#id_delete').value;

  const res = await fetch(`${api}/delete`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ id })
  });

  const msg = await res.json();
  document.querySelector('#mensagem').textContent = msg.mensagem || msg.erro;
  e.target.reset();
  carregarJogos();
});

async function carregarJogos() {
  const res = await fetch(`${api}/games`);
  const dados = await res.json();
  const ul = document.querySelector('#lista-jogos');
  ul.innerHTML = '';
  dados.forEach(jogo => {
    const li = document.createElement('li');
    li.textContent = `#${jogo.id} - ${jogo.nome} (${jogo.categoria} - ${jogo.ano})`;
    ul.appendChild(li);
  });
}

carregarJogos();
