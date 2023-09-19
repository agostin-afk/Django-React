'use client'
 
import { useEffect } from 'react'
import Image from 'next/image'
import styles from './page.module.css'
import React from 'react';
import axios from 'axios';
import { useRef } from 'react';

export default function Home() {
  const [dadosAPI, setDadosAPI, setFeedbackMessage] = React.useState([]);
  const filesElement = useRef(null);
  const sendFile = async () => {
    const dataForm = new FormData();
    for (const file of filesElement.current.files) {
      dataForm.append('file', file);
    }
    const res = await fetch(`http://127.0.0.1:8000/arquivos/`, {
      method: 'POST',
      body: dataForm,
    });
    const data = await res.json();
    console.log(data);
  };
  React.useEffect(() =>{ 
    fetch('http://127.0.0.1:8000/arquivos/') //Trocar pelo domínio da api que deseja 
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
      <h1>Enviar arquivo</h1>
      <form method="POST" action="http://127.0.0.1:8000/arquivos/">
        <div>
          <label>nome: </label>
          <input type='text' name='nome'></input>
          <br/>
          <label>arquivo: </label>
          <input type='file' name="arquivo"/>
          <br/>
          <br/>
        </div>
        <button onClick={sendFile}>Enviar</button>
      </form>
    </div>
  )
}