$( document ).ready(function() {

    const label = document.querySelectorAll('label.requiredField');
    const div = document.querySelectorAll('div.form-group');
    const input = document.querySelectorAll('.textinput.textInput.form-control');
    const small = document.querySelectorAll('.form-text.text-muted');
  
    
    label[0].style.display = 'none'
    input[0].placeholder = 'Usuário'
    input[0].autocomplete = 'off'
    input[0].classList.toggle('index')
    div[0].classList.toggle('index')
    
    label[1].style.display = 'none'
    input[1].placeholder = 'Senha'
    input[1].classList.toggle('index')
    div[1].classList.toggle('index')

    label[2].style.display = 'none'
    input[2].placeholder = 'Confirmar Senha'
    input[2].classList.toggle('index')
    div[2].classList.toggle('index')

    small[0].style.display = 'none'
    small[1].style.display = 'none'
    small[2].style.display = 'none'
    
    
});