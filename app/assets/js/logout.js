document.querySelector("#logout").addEventListener("submit", (e) => {
    e.preventDefault()
    
    try{
        localStorage.clear()

        window.location.href = "/"
    }
    catch {
        throw new Error("Falha ao deslogar");
    }
})