
const api_url = 'http://127.0.0.1:8000/';

export async function fetchPersonagem() {
  const url = `${api_url}personagens`; 
  const response = await fetch(url);  
  const data = await response.json();  
  return data;
}

export async function fetchFilmes() {
  const url = `${api_url}filmes`; 
  const response = await fetch(url);  
  const data = await response.json();
  return data;
}

export const fetchFilmeCenario = async (id) => {
  const response = await fetch(`http://127.0.0.1:8000/cenarios/${id}`);
  const data = await response.json();
  return data;
};

export const fetchFilmePersonagens = async (id) => {
  const response = await fetch(`http://127.0.0.1:8000/personagens/${id}`);
  const data = await response.json();
  return data;
};

