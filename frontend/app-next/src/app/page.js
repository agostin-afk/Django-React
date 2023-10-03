'use client'

import React from 'react';

export default function Home() {
  const [dadosAPI, setDadosAPI] = React.useState([]);

  React.useEffect(() => {
    fetch('http://127.0.0.1:8000/produtos/') //Trocar pelo domínio da api que deseja 
      .then((resposta) => {
        return resposta.json();
      })
      .then((resposta) => {
        setDadosAPI(resposta);
        console.log('resposta convertida de categorias', resposta)
      })
  }, [])
  return (
    <form action="http://127.0.0.1:8000/produtos/" method="post">
    <label>Nome:</label>
    <input type="text" id="nome" name="nome" required/><br/>

    <label>Descrição:</label>
    <textarea id="descricao" name="descricao" rows="4" cols="50" required></textarea><br/>

    <label>Preço:</label>
    <input type="number" id="preco" name="preco" step="0.01" required/><br/>

    <input type="submit" value="Enviar"/>
</form>
  )
}

