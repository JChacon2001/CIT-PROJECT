
document.querySelectorAll("answer").forEach(change => {
    change.addEventListener('click', function(){
        document.querySelector("answer").innerHTML = "flipped"
    })
})