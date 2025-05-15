const flipAudio = new Audio('/static/pageturn.mp3');


function flipCard(cardElement) {
    flipAudio.currentTime = 0;
    flipAudio.play();
    
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
  

