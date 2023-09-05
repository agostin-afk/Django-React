'use client'
 
import { useEffect } from 'react'
import Image from 'next/image'
import styles from './page.module.css'
import React from 'react';
import axios from 'axios';

export default function Home() {
  const [dadosAPI, setDadosAPI] = React.useState([]);
  
  React.useEffect(() =>{ 
    fetch('http://127.0.0.1:8000/categorias/?format=json') //Trocar pelo domínio da api que deseja 
      .then((resposta) => {
          return resposta.json();
      })
      .then((respostaP) => {
          setDadosAPI(respostaP);
          console.log('resposta convertida',respostaP)
      })
      .finally(() =>{
        console.log(dadosAPI);
      })
  }, [])
  console.log('dados da API',dadosAPI);
  
  return (
    <div>
      {dadosAPI.map((item, index) => ( // Pode trocar o "item" por "produto" por exemplo, trocando também os que estão dentro das chaves
        <div key={index}>
          <p>O item de id {item.id} é {item.nome}</p><p>E possui a seguinte descrição: {item.descricao}</p>
        </div>
      ))}
    </div>
  )
}
