function flipCard(cardElement) {
    if(cardElement.classList.contains('unflipped')) {
        cardElement.classList.add('flip');
        cardElement.classList.remove('unflipped');

      }
    else { 
        cardElement.classList.add("unflipped");
        cardElement.classList.remove('flip')

    }
}

document.querySelectorAll(".answer").forEach(change => {
    change.addEventListener('click', function(){
        flipCard(this)
    })
})

function toggleSidebar() {
    const sidebar = document.getElementById('sidebar');
    sidebar.classList.toggle('collapsed');
  }
  