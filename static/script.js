
document.querySelectorAll("answer").forEach(change => {
    change.addEventListener('click', function(){
        document.querySelector("answer").innerHTML = "flipped"
    })
})

function flipCard(cardElement) {
    cardElement.querySelector('.flip-card-inner').classList.toggle('flipped');
  }
  