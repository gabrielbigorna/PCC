$( document ).ready(function() {
    
    const btn_link = document.querySelector('.delete-btn');
    const modal = document.querySelector('.box-modal');
    const btn_csl = document.querySelector('.dlt-btn-modal-csl');
    const btn_cfm = document.querySelector('.dlt-btn-modal-cfm');
    
    $(btn_link).on('click', function(e) {

        e.preventDefault();
        modal.style.display = "flex"
        var dltLink = $(this).attr('href');

        $(btn_cfm).on('click', function() {
    
            console.log("deletar");
            window.location.href = dltLink;
    
        });
        
        $(btn_csl).on('click', function() {
    
            console.log("cancelar");
            modal.style.display = "none"
    
        });
    });

    
});