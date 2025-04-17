

//adicionar? --> document.addEventListener('DOMContentLoaded', function() {

  //Versão mais simples:
  setTimeout(function() {
    const mensagem = document.querySelector('.lista-sucesso-erro');
    if (mensagem) {
      mensagem.style.display = 'none';
    }
  }, 2000);

/*versão com forEach:  
setTimeout(function() {
    const mensagem = document.querySelectorAll('.lista-sucesso-erro');
    mensagem.forEach(aviso => {
      aviso.style.display = 'none';
    });
  }, 3000);
*/


  /*versão mais completa com DOMContentLoaded e FADEOUT:
  document.addEventListener('DOMContentLoaded', function() {
    setTimeout(function() {
      const mensagem = document.querySelector('.lista-sucesso-erro-epi');
      if (mensagem) {
        mensagem.classList.add('esconder'); <-------------------------------------------------
        setTimeout(() => {
          mensagem.style.display = 'none';
        }, 1000); // tempo do fade
      }
    }, 3000);
  });*/