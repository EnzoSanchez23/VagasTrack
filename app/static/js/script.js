const status_text = document.getElementsByClassName("texto-status");
const cor_verde = "#16A34A";
const cor_amarelo = "#CA8A04";
const cor_vermelho = "#DC2626";


for(let i = 0; i < status_text.length; i++){
    if(status_text[i].innerHTML === "Aprovado"){
        status_text[i].style.backgroundColor = cor_verde;
        status_text[i].style.borderColor = cor_verde;
    }

    if(status_text[i].innerHTML === "Em Processo"){
        status_text[i].style.backgroundColor = cor_amarelo;
        status_text[i].style.borderColor = cor_amarelo;
    }

    if(status_text[i].innerHTML === "Encerrado"){
        status_text[i].style.backgroundColor = cor_vermelho;
        status_text[i].style.borderColor = cor_vermelho;
    }
}

