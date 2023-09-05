'use client'
 
import { useEffect } from 'react'
import Image from 'next/image'
import styles from './page.module.css'
import React from 'react';
import axios from 'axios';

export default function Home() {
  const [dadosGithub, setDadosdoGithub] = React.useState([]);
  
  React.useEffect(() =>{ 
    fetch('http://127.0.0.1:8000/categorias/?format=json')
      .then((resposta) => {
          return resposta.json();
      })
      .then((respostaP) => {
          setDadosdoGithub(respostaP);
          console.log('resposta convertida',respostaP)
      })
      .finally(() =>{
        console.log(dadosGithub);
      })
  }, [])
  console.log('dados do github',dadosGithub);
  
  return (
    <div>
      {dadosGithub.map((item, index) => (
        <div key={index}>
          <p>O item de id {item.id} é {item.nome}</p><p>E possui a seguinte descrição: {item.descricao}</p>
        </div>
      ))}
    </div>
  )
}
