$(document).ready(function () {
  // Filtreleme Formunu Temizle
  $("#clearFilter").on("click", () => {
    $(`#filterForm`).find("input, select, textarea").prop("value", "");
  });
});
