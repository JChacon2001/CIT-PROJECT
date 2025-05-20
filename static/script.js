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
  
function toggleContent(id) {
    var el = document.getElementById("content-" + id);
    if (el.style.display === "none" || el.style.display === "") {
        el.style.display = "block";
    } else {
        el.style.display = "none";
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const toggleBtn = document.getElementById("toggle-theme");
    const themeIcon = document.getElementById("theme-icon");
    const root = document.documentElement;
  
    function applyTheme(isDark) {
      if (isDark) {
        root.classList.add("dark-mode");
      } else {
        root.classList.remove("dark-mode");
      }
  
      if (themeIcon) {
        themeIcon.className = isDark ? "fas fa-sun" : "fas fa-moon";
      }
    }
  
    // Load theme on first page load
    const savedTheme = localStorage.getItem("theme");
    applyTheme(savedTheme === "dark");
  
    // Toggle when clicked
    if (toggleBtn) {
      toggleBtn.addEventListener("click", () => {
        const isDarkNow = root.classList.toggle("dark-mode");
        localStorage.setItem("theme", isDarkNow ? "dark" : "light");
        applyTheme(isDarkNow);
      });
    }
  });
  


function toggleCourse(courseId) {
  const content = document.getElementById(`course-${courseId}`);
  const arrow = content.previousElementSibling.querySelector('.toggle-arrow');
  if (content.style.display === "none" || content.style.display === "") {
    content.style.display = "block";
    arrow.textContent = "▼";
  } else {
    content.style.display = "none";
    arrow.textContent = "▼";
  }
}


function openCourseModal() {
  document.getElementById("courseModal").style.display = "flex";
}

function closeCourseModal() {
  document.getElementById("courseModal").style.display = "none";
}

