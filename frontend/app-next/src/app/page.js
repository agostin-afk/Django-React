'use client'

import React from 'react';

export default function Home() {
  const [dadosAPI, setDadosAPI] = React.useState([]);

  React.useEffect(() => {
    fetch('http://127.0.0.1:8000/categorias/?format=json') //Trocar pelo domínio da api que deseja 
      .then((resposta) => {
        return resposta.json();
      })
      .then((resposta) => {
        setDadosAPI(resposta);
        console.log('resposta convertida de categorias', resposta)
      })
  }, [])
  return (
    <div>
      {dadosAPI.map((categoria, indexCategoria) => (
        <div key={indexCategoria}>
          <p>
            Categoria de nome {categoria.nome} existe e possui o numero {categoria.id}
          </p>
        </div>
      ))}
    </div>
  )
}

