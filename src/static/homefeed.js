// Side bar
const menuItems = document.querySelectorAll('.menu-item');
// remove active class
const changeActiveItem = ()=>{
    menuItems.forEach(item=>{
        item.classList.remove("active");
        if(window.innerWidth<922){
        messages.style.display = "none";}else{
            messages.style.display = "block";
        }
    })
}
menuItems.forEach(item=>{
    item.addEventListener('click',()=>{
        changeActiveItem();
        item.classList.add("active");
        if(item.id!="notifications"){
            document.querySelector(".notification-popup").style.display = 'none'
        }else{
            document.querySelector(".notification-popup").style.display = 'block'
            document.querySelector("#notifications .notification-count").style.display='none'
        }
    })
})

//messages logic
const messagesNotification = document.querySelector("#messages-notifications");
const messages = document.querySelector(".messages");
const message = messages.querySelectorAll(".message");
const messageSearch = document.querySelector("#message-search");

messagesNotification.addEventListener("click",()=>{
    messages.style.boxShadow = '0 0 1rem var(--color-primary)'
    messages.style.display = "block"
    messagesNotification.querySelector(".notification-count").style.display = 'none'
    setTimeout(()=>{messages.style.boxShadow = 'none'},2000)
})

// search chat
const searchMessage=()=>{
    const val = messageSearch.value.toLowerCase();
    message.forEach(chat =>{
        let name = chat.querySelector('h5').textContent.toLowerCase();
        if(name.indexOf(val)!=-1){
            chat.style.display ="flex";
        }else{
            chat.style.display ="none";
        }
    })
}
messageSearch.addEventListener("keyup",searchMessage)