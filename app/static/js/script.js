let modal_div = document.getElementById("modal-div");

function openModal() {
    console.log("abrindo modal");
    modal_div.style.display = "flex";
}

function closeModal() {
    console.log("fechando modal");
    modal_div.style.display = "none";
}