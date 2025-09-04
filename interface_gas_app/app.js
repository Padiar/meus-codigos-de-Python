const output = document.getElementById("output");

function mostrarResultado(data) {
  output.textContent = JSON.stringify(data, null, 2);
}

function trocarGas() {
  fetch("/trocar", { method: "POST" })
    .then(res => res.json())
    .then(mostrarResultado);
}

function usarGas() {
  fetch("/usar", { method: "POST" })
    .then(res => res.json())
    .then(mostrarResultado);
}

function verStatus() {
  fetch("/status")
    .then(res => res.json())
    .then(mostrarResultado);
}

function verPrevisao() {
  fetch("/previsao")
    .then(res => res.json())
    .then(mostrarResultado);
}