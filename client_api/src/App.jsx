import { useState, useEffect } from 'react';
import './App.css';

import { fetchPersonagem } from '../wrapper.js';

function App() {
  //     #variavel    #funcão          #estado inicial
  const [personagens, setPersonagem] = useState([]);
  const [loading, setLoading] = useState(false);

  
  const loadPersonagens = async () => {
    setLoading(true);
    try {
      const data = await fetchPersonagem();
      setPersonagem(data); 
    } catch (error) {
      alert('Erro ao carregar os personagens.');
    } finally {
      setLoading(false);
    }
  };

  // Chama loadPersonagens quando o componente for montado
  useEffect(() => {
    loadPersonagens();
  }, []);

  return (
    <>
      <div>
        {loading ? (
          <div>Carregando...</div>
        ) : (
          Array.isArray(personagens) && personagens.length > 0 ? (
            <ul>
              {personagens.map((personagem, index) => (
                <li key={index}>
                  <p><strong>Nome:</strong> {personagem.nome}</p>
                  <p><strong>Descrição:</strong> {personagem.descricao}</p>
                  <p><strong>Foto:</strong> <img src={personagem.foto} alt={personagem.nome} style={{width: '150px', height: '150px'}} /></p>
                </li>
              ))}
            </ul>
          ) : (
            <div>Sem personagens disponíveis.</div>
          )
        )}
      </div>
    </>
  );
}

export default App;
