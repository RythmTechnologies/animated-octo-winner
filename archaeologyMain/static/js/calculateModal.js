function calculateTotalPrice(modalId) {
  const piece = document.querySelector('#' + modalId + ' #id_piece');
  const unitprice = document.querySelector('#' + modalId + ' #id_unitprice');
  const taxrate = document.querySelector('#' + modalId + ' #id_taxrate');
  const totalprice = document.querySelector('#' + modalId + ' #id_totalprice');

  if (piece && unitprice && taxrate && totalprice) {
      const pieceValue = parseInt(piece.value) || 0;
      const unitpriceValue = parseFloat(unitprice.value) || 0;
      const taxrateValue = parseFloat(taxrate.value) || 0;

      const total = pieceValue * unitpriceValue * (1 + taxrateValue / 100);
      totalprice.value = total.toFixed(2);
  }
}

document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('[id^=updateModal]').forEach(function(modal) {
      modal.addEventListener('shown.bs.modal', function () {
          calculateTotalPrice(modal.id);
          // Form elemanlarında değişiklik olduğunda hesaplama fonksiyonunu tekrar çalıştır
          modal.querySelector('#id_piece').addEventListener('input', function() { calculateTotalPrice(modal.id); });
          modal.querySelector('#id_unitprice').addEventListener('input', function() { calculateTotalPrice(modal.id); });
          modal.querySelector('#id_taxrate').addEventListener('input', function() { calculateTotalPrice(modal.id); });
      });
  });
});