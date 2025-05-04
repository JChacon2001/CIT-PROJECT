function flipCard(cardElement) {
    if(cardElement.classList.contains('flipped')) {
        cardElement.classList.add('unflip');
        cardElement.classList.remove('flipped');
      }
    else { 
        cardElement.classList.add("flipped");
        cardElement.classList.remove('unflip')
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
  