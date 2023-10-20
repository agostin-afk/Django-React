'use client'

import React from 'react';

export default function Home() {
  const [dadosAPI, setDadosAPI] = React.useState([]);

  React.useEffect(() => {
    method: 'POST',
    fetch('http://127.0.0.1:8000/usuarios/') //Trocar pelo domínio da api que deseja 
      .then((resposta) => {
        return resposta.json();
      })
      .then((resposta) => {
        setDadosAPI(resposta);
        console.log('resposta convertida', resposta)
      })
  }, [])
  return (
   <div>
{/*   {dadosAPI.map((item, index) => (
    <div key={index}>

    </div>
  ))} */}
                <form action="http://127.0.0.1:8000/usuarios/" method="POST"/>
                    Seu nome:
                    <input type="text" placeholder="Seu nome" name="username"/>
                    <br/>
                    <br/>
                    Sua senha:
                    <input type="password" placeholder="Sua senha" name="senha"/>
                    <br/>
                    <br/>
                    Seu Email:
                    <input type="email" placeholder="Seu email" name="email"/>
                    <br/>
                    <br/>
                    <a href="http://127.0.0.1:8000/auth/login/" target="_self">Se já é cadastrado, clique aqui!!</a>
                    <br/>
                    <input type="submit" value= "Cadastrar"></input>
</div>

  )
}

