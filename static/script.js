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

function flipping(card){
    card.classList.add = 'rotateY(180%)'
}

document.querySelectorAll(".answer").forEach(change => {
    change.addEventListener('click', function(){
        flipCard(this)
    })
})