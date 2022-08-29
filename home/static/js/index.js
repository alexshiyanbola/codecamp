let body = document.querySelector('body')
let swap = document.querySelector('.swap')
let icon = document.querySelector('.bi-moon-fill')

swap.addEventListener('click', ()=>{
  body.classList.toggle('dark')
  if (body.classList.contains('dark')){
    icon.classList.replace("bi-moon-fill", "bi-sun-fill")
  }
  else{
        icon.classList.replace("bi-sun-fill","bi-moon-fill")
    }
})
