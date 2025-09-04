const output = document.getElementById("output");

// ✅ Função única para formatar data em português, com ou sem hora
function formatoDataHoraBr(isoString, comHora = true) {
  const data = new Date(isoString);
  const opcoes = {
    day: "2-digit",
    month: "2-digit",
    year: "numeric",
    ...(comHora && { hour: "2-digit", minute: "2-digit" }),
    timeZone: "America/Sao_Paulo"
  };
  return data.toLocaleString('pt-BR', opcoes);
}

// ✅ Trocar gás: exibe data e hora atual formatada
function trocarGas() {
  fetch("/trocar", { method: "POST" })
    .then(res => res.json())
    .then(data => {
      const dataIso = data.mensagem.match(/\d{4}-\d{2}-\d{2}/)?.[0];
      const agora = new Date().toISOString();
      const dataBr = formatoDataHoraBr(agora);
      output.textContent = dataIso
        ? `Gás trocado em ${dataBr}.`
        : data.mensagem;
    });
}

// ✅ Registrar uso do gás: exibe data e hora do uso
function usarGas() {
  fetch("/usar", { method: "POST" })
    .then(res => res.json())
    .then(data => {
      const isoCompleto = data.mensagem.match(/\d{4}-\d{2}-\d{2}T\d{2}:\d{2}/)?.[0];
      const dataBr = isoCompleto ? formatoDataHoraBr(isoCompleto) : "";
      output.textContent = dataBr
        ? `Uso registrado em ${dataBr}.`
        : data.mensagem;
    });
}

// ✅ Ver status: formata todos os campos de data (array, objeto, string)
function verStatus() {
  fetch("/status")
    .then(res => res.json())
    .then(data => {
      if (Array.isArray(data.dias_uso)) {
        data.dias_uso = data.dias_uso.map(d => formatoDataHoraBr(d));
      }

      if (Array.isArray(data.trocas)) {
        data.trocas = data.trocas.map(t => ({
          ...t,
          data: formatoDataHoraBr(t.data, false)
        }));
      }

      if (data.ultima_troca) {
        data.ultima_troca = formatoDataHoraBr(data.ultima_troca, false);
      }

      output.textContent = JSON.stringify(data, null, 2);
    });
}

// ✅ Ver previsão: mostra resumo em texto formatado
function verPrevisao() {
  fetch("/previsao")
    .then(res => res.json())
    .then(data => {
      if (data.erro) {
        output.textContent = data.erro;
        return;
      }

      let aviso = data.aviso ? `⚠️ ${data.aviso}\n\n` : "";
      let dataFormatada = formatoDataHoraBr(data.ultima_troca, false);

      let texto = `${aviso}Última troca: ${dataFormatada}
Dias usados: ${data.dias_usados}
Média de duração: ${data.media_duracao.toFixed(1)} dias
Dias restantes estimados: ${data.dias_restantes}`;

      output.textContent = texto;
    });
}
