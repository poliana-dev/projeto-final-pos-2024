
const api_url = 'http://127.0.0.1:8000/';

export async function fetchPersonagem() {
  const url = `${api_url}personagens`; 
  const response = await fetch(url);  
  const data = await response.json();  
  return data;
}

