function flipCard(cardElement) {
    cardElement.classList.toggle('flipped');
    if(cardElement.classList.contains('flipped')) {
        cardElement.classList.add('unflip');
        setTimeout(function(){
          cardElement.classList.remove('flipped', 'unflip');
        }, 500);
      }
      else { 
        cardElement.classList.add("flipped");
      }
}


document.querySelectorAll(".answer").forEach(change => {
    change.addEventListener('click', function(){
        flipCard(this)
    })
})