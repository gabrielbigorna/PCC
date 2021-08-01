$( document ).ready(function() {

    const label_ttl = document.getElementsByName("title");
    const label_dcp = document.getElementsByName("description");
    
    label_ttl[0].placeholder = 'Título'
    label_ttl[0].autocomplete = 'off'
    label_ttl[0].classList.toggle('index', false) 
    
    label_dcp[0].placeholder = 'Descrição'
    
    
});