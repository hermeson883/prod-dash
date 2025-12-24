async function handleFormData(event) {
    event.preventDefault(); // ESSENCIAL

    // Sempre o <form>, nunca o botão
    const form = event.currentTarget;
    const formdata = new FormData(form);

    try {
        const response = await fetch("http://127.0.0.1:8000/login", {
            method: "POST",
            body: formdata
        });
        if (!response.ok) {
            alert("Usuário ou senha inválidos");
            return;
        }

        const result = await response.json();
        window.location.href = "/dashboard";

    } catch (error) {
        alert("Estamos com problemas técnicos");
        console.error(error);
    }
}

document
    .querySelector("#loginForm")
    ?.addEventListener("submit", handleFormData);
