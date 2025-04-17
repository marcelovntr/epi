
  setTimeout(function() {
    const mensagem = document.querySelectorAll('.lista-sucesso-erro');
    mensagem.forEach(aviso => {
      aviso.style.display = 'none';
    });
  }, 3000);

  /*Versão mais simples:
  setTimeout(function() {
    const mensagem = document.querySelector('.lista-sucesso-erro');
    if (mensagem) {
      mensagem.style.display = 'none';
    }
  }, 3000);*/