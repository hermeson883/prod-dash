async function handleFormData(event) {
    event.preventDefault()

    // Sempre o <form>, nunca o botão
    const form = event.currentTarget
    const formdata = new FormData(form)

    try {
        const response = await fetch("http://127.0.0.1:8000/login", {
            method: "POST",
            body: formdata
        })
        if (!response.ok) {
            alert("Usuário ou senha inválidos")
            return
        }

        const result = await response.json()

        // Salva o token e username
        localStorage.setItem("username", result.username)
        localStorage.setItem("token", result.token)

        window.location.href = "/dashboard"

    } catch (error) {
        alert("Estamos com problemas técnicos")
        console.error(error)
    }
}

document
    .querySelector("#loginForm")
    ?.addEventListener("submit", handleFormData)
