function confirmarExclusao(id) {
  const swalWithBootstrapButtons = Swal.mixin({
    customClass: {
      confirmButton: "btn btn-success",
      cancelButton: "btn btn-danger",
    },
    buttonsStyling: false,
  });

  swalWithBootstrapButtons
    .fire({
      title: "Quer mesmo deletar o colaborador?",
      text: "Não será possível desfazer a ação!",
      icon: "warning",
      showCancelButton: true,
      confirmButtonText: "Sim, deletar!",
      cancelButtonText: "Não, cancelar!",
      reverseButtons: true,
    })
    .then((result) => {
      if (result.isConfirmed) {
        swalWithBootstrapButtons
          .fire({
            title: "Deletado!",
            text: "O colaborador foi deletado.",
            icon: "success",
            timer: 1200,
            showConfirmButton: false,
          })
          .then(() => {
            document.getElementById("form-excluir-" + id).submit();
          });
      } else if (result.dismiss === Swal.DismissReason.cancel) {
        swalWithBootstrapButtons.fire({
          title: "Cancelado",
          text: "A exclusão foi cancelada.",
          icon: "error",
        });
      }
    });
}

console.log("JS funcionando!");

function confirmarExclusaoEpi(id) {
  const swalWithBootstrapButtons = Swal.mixin({
    customClass: {
      confirmButton: "btn btn-success",
      cancelButton: "btn btn-danger",
    },
    buttonsStyling: false,
  });

  swalWithBootstrapButtons
    .fire({
      title: "Quer mesmo deletar o EPI?",
      text: "Não será possível desfazer a ação!",
      icon: "warning",
      showCancelButton: true,
      confirmButtonText: "Sim, deletar!",
      cancelButtonText: "Não, cancelar!",
      reverseButtons: true,
    })
    .then((result) => {
      if (result.isConfirmed) {
        swalWithBootstrapButtons
          .fire({
            title: "Deletado!",
            text: "O EPI foi deletado.",
            icon: "success",
            timer: 1200,
            showConfirmButton: false,
          })
          .then(() => {
            document.getElementById("form-excluir2-" + id).submit();
          });
      } else if (result.dismiss === Swal.DismissReason.cancel) {
        swalWithBootstrapButtons.fire({
          title: "Cancelado",
          text: "A exclusão foi cancelada.",
          icon: "error",
        });
      }
    });
}

/*ALERTA ANTERIOR MAIS SIMPLES
function confirmarExclusaoEpi(id) {
    Swal.fire({
        title: 'Quer mesmo excluir o EPI?',
        text: 'Essa ação não poderá ser desfeita!',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonText: 'Excluir',
        cancelButtonText: 'Cancelar',
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6'
        // customClass: {
        //     popup: 'swal-pequeno'
        //   }
    }).then((result) => {
        if (result.isConfirmed) {
            document.getElementById('form-excluir-' + id).submit();
        }
    });
}
*/
console.log("JS funcionando2222!");

// .swal-pequeno {
//     width: 300px !important; /* tamanho reduzido */
//     font-size: 0.9rem;       /* texto um pouco menor */
//   }
