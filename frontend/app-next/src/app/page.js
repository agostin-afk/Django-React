'use client'
 
import { useEffect } from 'react'
import Image from 'next/image'
import styles from './page.module.css'
import React from 'react';

export default function Home() {
  const [dadosGithub, setDadosdoGithub] = React.useState({});
  
  React.useEffect(() =>{ 
    fetch('https://api.github.com/users/agostin-afk')
      .then((resposta) => {
          return resposta.json();
      })
      .then((respostaP) => {
          setDadosdoGithub(respostaP);
          console.log('resposta convertida',respostaP)
      })
  }, [])
  console.log('dados do github',dadosGithub);
  return (
    <div>
   {dadosGithub.login} <br/>
   {dadosGithub.name}
   <br/>
   {dadosGithub.public_repos}
   </div>

  )
}
