const container = document.getElementById('container');
const registerBtn = document.getElementById('register');
const loginBtn = document.getElementById('login');

registerBtn.addEventListener('click', () => {
    container.classList.add("active");
});

loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
});

function toggleTextField() {
    var textField = document.getElementById("familyTextField");
    var checkbox = document.getElementById("cbx-12");
    
    if (checkbox.checked) {
        textField.style.display = "block";
    } else {
        textField.style.display = "none";
    }
}



document.addEventListener('DOMContentLoaded', function () {
    const closeButtons = document.querySelectorAll('.close-btn');
    closeButtons.forEach(button => {
        button.addEventListener('click', function () {
            const flashMessage = this.parentNode;
            flashMessage.classList.remove('fade');
            setTimeout(() => {
                flashMessage.remove();
            }, 500); // Adjust the timeout to match your CSS transition duration
        });
    });
});