let modal_div = document.getElementById("modal-div");

function editarVaga(btn){

    const linha = btn.closest("tr");
    const colunas = linha.querySelectorAll("td");

    const vaga = colunas[0].textContent;
    const empresa = colunas[1].textContent;
    const local = colunas[2].textContent;
    const salario = colunas[3].textContent;
    const modelo = colunas[4].textContent.trim();
    const status = colunas[5].textContent.trim();

    document.getElementById("vaga-input-modal").value = vaga;
    document.getElementById("empresa-input-modal").value = empresa;
    document.getElementById("local-input-modal").value = local;
    document.getElementById("salario-input-modal").value = salario;
    document.getElementById("modelo-input-modal").value = modelo;
    document.getElementById("status-input-modal").value = status;

    openModal();
}

function openModal() {
    console.log("abrindo modal");
    modal_div.style.display = "flex";
}

function closeModal() {
    console.log("fechando modal");
    modal_div.style.display = "none";
}