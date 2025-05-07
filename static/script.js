function flipCard(cardElement) {
    if(cardElement.classList.contains('flipped')) {
        cardElement.classList.add('unflip');
        cardElement.classList.remove('flipped');
        cardElement.flipping(this)
      }
    else { 
        cardElement.classList.add("flipped");
        cardElement.classList.remove('unflip')
        cardElement.flipping(this)
    }
}

function flipping(card){
    card.style.transform = "rotateY(180deg)"
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
  