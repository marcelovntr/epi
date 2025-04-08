function confirmarExclusao(id) {
    Swal.fire({
        title: 'Quer mesmo excluir o colaborador?',
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

console.log("JS funcionando!");

// .swal-pequeno {
//     width: 300px !important; /* tamanho reduzido */
//     font-size: 0.9rem;       /* texto um pouco menor */
//   }