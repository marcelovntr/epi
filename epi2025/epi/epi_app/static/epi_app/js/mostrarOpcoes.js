document.addEventListener("DOMContentLoaded", 
    function () {
    const statusSelecionado = document.getElementById("status-selecionado");
    const camposCondicionais = document.getElementById("campos-condicionais");

    statusSelecionado.addEventListener("change", function () {
      const valor = this.value;
      if (["devolvido", "perdido", "danificado"].includes(valor)) {
        camposCondicionais.hidden = false;
      } else {
        camposCondicionais.hidden = true;
      }
    });
  });