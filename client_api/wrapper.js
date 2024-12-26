
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

export const fetchFilmeAcessorio = async (id) => {
  const response = await fetch(`http://127.0.0.1:8000/acessorios/${id}`);
  const data = await response.json();
  return data;
};


export async function fetchCenario() {
  const url = `${api_url}cenarios`; 
  const response = await fetch(url);  
  const data = await response.json();
  return data;
};

export async function fetchMusica() {
  const url = `${api_url}musicas`; 
  const response = await fetch(url);  
  const data = await response.json();
  return data;
};

export async function fetchFilmesMusica(id) {
  const url = `${api_url}filmes/${id}`; 
  const response = await fetch(url);  
  const data = await response.json();
  return data;
}



