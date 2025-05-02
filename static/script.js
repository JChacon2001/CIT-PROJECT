document.addEventListener("DOMContentLoaded", function () {
    const card = document.querySelector(".flip-card");
    card.addEventListener("click", function () {
      card.querySelector(".flip-card-inner").classList.toggle("flipped");
    });
  });
  
  function flipCard(card) {
    card.classList.toggle('flipped');
  }
  