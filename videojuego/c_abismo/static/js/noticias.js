$(function(){
  const $zona = $("#zona-noticias");
  const $msg  = $("#msg");

  function msg(t, ok=false){
    $msg.text(t).css("color", ok ? "#8f8" : "#f88").show();
  }

  function tarjetizar(n) {
    const titulo = n.title || "Sin título";
    const desc   = n.short_description || "";
    const img    = n.thumbnail || "https://via.placeholder.com/400x225?text=Sin+imagen";
    const link   = n.article_url || n.url || "#";
    const fecha  = n.published_date || n.date || "";
    return `
      <div class="col-12 col-md-6 col-lg-4">
        <div class="card h-100">
          <img src="${img}" class="card-img-top" alt="${titulo}">
          <div class="card-body d-flex flex-column">
            <h5 class="card-title">${titulo}</h5>
            <span class="badge badge-date mb-2">${fecha}</span>
            <p class="card-text flex-grow-1">${desc}</p>
            <a class="btn btn-sm btn-warning mt-auto" href="${link}" target="_blank" rel="noopener">Leer más</a>
          </div>
        </div>
      </div>
    `;
  }

  function cargar() {
    $msg.hide();
    $zona.empty();
    $.get("/api/noticias/", function(data){
      if(!Array.isArray(data) || data.length === 0){
        msg("No hay noticias disponibles.", true);
        return;
      }
      // Limita si quieres, ej. a 24
      const items = data.slice(0, 24).map(tarjetizar).join("");
      $zona.html(items);
    }).fail(function(xhr){
      console.error("Error noticias:", xhr.status, xhr.responseText);
      msg("Error al cargar noticias.");
    });
  }

  $("#btnRecargar").on("click", cargar);
  cargar();
});