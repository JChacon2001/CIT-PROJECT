function flipCard(cardElement) {
    cardElement.classList.toggle('flipped');
}


document.querySelectorAll(".answer").forEach(change => {
    change.addEventListener('click', function(){
        flipCard(this)
    })
})