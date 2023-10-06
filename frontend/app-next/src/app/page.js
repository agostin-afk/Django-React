'use client'

import React from 'react';

export default function Home() {
  const [dadosAPI, setDadosAPI] = React.useState([]);

  React.useEffect(() => {
    fetch('http://127.0.0.1:8000/imagens/?format=json') //Trocar pelo domínio da api que deseja 
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
      {dadosAPI.map((item, index) => ( // Pode trocar o "item" por "produto" por exemplo, trocando também os que estão dentro das chaves
        <div key={index}>
          <p>teste</p>
          <image source={item.foto} />
        </div>
      ))}
    </div>

  )
}

