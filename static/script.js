document.querySelectorAll(".carddeck").forEach(flip => {
    
    flip.addEventListener('click', function(){

        if (this.innerHTMl == "flipped"){
            this.innerHTML = "unflipped"
        }
        else{
            this.innerHTML = "flipped" 
            this.innerHTML += `<button id="flip"> flip </button>`
        }
        

        
        
        
    })
})