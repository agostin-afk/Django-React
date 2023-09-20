'use client'

import React from 'react';

export default function Home() {
  const [dadosAPI, setDadosAPI] = React.useState([]);
  const [dadosProdutos, setDadosProdutos] = React.useState([]);

  React.useEffect(() => {
    fetch('http://127.0.0.1:8000/categorias/?format=json') //Trocar pelo domínio da api que deseja 
      .then((resposta) => {
        return resposta.json();
      })
      .then((resposta) => {
        setDadosAPI(resposta);
        console.log('resposta convertida de categorias', resposta)
      }),
      fetch('http://127.0.0.1:8000/produtos/?format=json')
        .then((respostaProdutos) => {
          return respostaProdutos.json();
        })
        .then((respostaProdutos) => {
          setDadosProdutos(respostaProdutos);
          console.log('resposta convertida de produtos', respostaProdutos)
        })
  }, [])
  return (
    <div>
      {dadosAPI.map((categoria, indexCategoria) => (
        <div key={indexCategoria}>
          <p>
            Categoria de nome {categoria.nome} existe e possui o numero {categoria.id}
          </p>
          {dadosProdutos.filter((produto) => produto.categoria === categoria.id)
            .map((produtoFiltrado, indexProduto) => (
          <p key={indexProduto}>
            Existe um produto {produtoFiltrado.nome} e esse produto tem a categoria {produtoFiltrado.categoria}
          </p>
        ))}
        </div>
      ))}
    </div>
  )
}

