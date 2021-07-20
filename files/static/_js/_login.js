$( document ).ready(function() {

    const label = document.querySelectorAll('label.requiredField');
    const div = document.querySelectorAll('div.form-group');
    const input = document.querySelectorAll('.textinput.textInput.form-control');
      
    
    label[0].style.display = 'none'
    input[0].placeholder = 'Usuário'
    input[0].autocomplete = 'off'
    input[0].classList.toggle('index')
    div[0].classList.toggle('index')
    
    label[1].style.display = 'none'
    input[1].placeholder = 'Senha'
    input[1].classList.toggle('index')
    div[1].classList.toggle('index')
    
    
});