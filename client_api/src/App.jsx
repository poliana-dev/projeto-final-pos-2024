import { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

import Personagens from "./components/personagens";
import Filmes from "./components/Filmes";


function App() {
  const [paginaAtual, setPaginaAtual] = useState("inicio");

  const renderPagina = () => {
    switch (paginaAtual) {
      case "inicio":
        return <h1>Bem-vindo à aplicação!</h1>;
      case "personagens":
        return <Personagens />;
      case "filmes":
        return <Filmes />;
      default:
        return <h1>Página não encontrada</h1>;
    }
  };

  return (
    <div>
      <ul className="nav nav-tabs">
        <li className="nav-item">
          <button
            className={`nav-link ${paginaAtual === "inicio" ? "active" : ""}`}
            onClick={() => setPaginaAtual("inicio")}
          >
            Início
          </button>
        </li>
        <li className="nav-item">
          <button
            className={`nav-link ${paginaAtual === "personagens" ? "active" : ""}`}
            onClick={() => setPaginaAtual("personagens")}
          >
            Personagens
          </button>
        </li>
        <li className="nav-item">
          <button
            className={`nav-link ${paginaAtual === "filmes" ? "active" : ""}`}
            onClick={() => setPaginaAtual("filmes")}
          >
            Filmes
          </button>
        </li>
      </ul>
      <div className="container mt-4">{renderPagina()}</div>
    </div>
  );
}

export default App;
