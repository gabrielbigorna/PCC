$( document ).ready(function() {
   const btn_back = document.querySelector('.btn-success');


    btn_back.addEventListener("click", (e) => {
        
        // e.preventDefault();
        console.log("Funcionou");
        history.back();
        

    })
});