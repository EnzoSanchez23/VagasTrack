let modal_div = document.getElementById("modal-div");

function editarVaga(btn) {

    const linha = btn.closest("tr");
    const colunas = linha.querySelectorAll("td");

    const id = colunas[0].textContent;
    const vaga = colunas[1].textContent;
    const empresa = colunas[2].textContent;
    const local = colunas[3].textContent;
    const salario = colunas[4].textContent;
    const modelo = colunas[5].textContent.trim();
    const status = colunas[6].textContent.trim();

    document.getElementById("id-input-modal").value = id;
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