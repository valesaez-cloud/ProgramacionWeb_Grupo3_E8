$(document).ready(function () {
  const $zona = $("#categorias");
  const $msg  = $("#msg");

  function msg(t, ok=false){
    $msg.text(t).css("color", ok ? "green" : "crimson").show();
  }

  $.get("/api/categorias/", function (data) {
    const cats = (data && data.categories) ? data.categories : [];
    if (!Array.isArray(cats) || cats.length === 0) {
      msg("No se encontraron categorías.", true);
      return;
    }

    cats.forEach(function (categoria) {
      const nombre = categoria.name || "Sin nombre";
      const img    = categoria.thumb || "https://via.placeholder.com/300x180?text=Sin+imagen";
      const desc   = categoria.description || "";

      $zona.append(`
        <div class="col-12 col-sm-6 col-md-4 col-lg-3">
          <div class="card h-100 shadow-sm">
            <img src="${img}" class="card-img-top" alt="${nombre}">
            <div class="card-body">
              <h5 class="card-title text-truncate">${nombre}</h5>
              <p class="card-text text-muted">${desc}</p>
            </div>
          </div>
        </div>
      `);
    });
  }).fail(function () {
    msg("Error al cargar las categorías.");
  });
});