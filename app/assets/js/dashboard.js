document.addEventListener("DOMContentLoaded", () => {
    
    const username = localStorage.getItem("username")

    console.log("sdafasdf", username)

    document.getElementById("userModalLabel").textContent = username

})