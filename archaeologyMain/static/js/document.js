function downloadOtherHTMLAsPDF(documentId) {
    if (confirm('Bu belgeyi PDF olarak indirmek istediğinize emin misiniz?')) {
        
        fetch(`get-html/${documentId}/`) 
            .then(response => response.text())
            .then(html => {
                
                var div = document.createElement('div');
                div.innerHTML = html;
                document.body.appendChild(div); 

                
                html2canvas(div).then(canvas => {
                    const imgData = canvas.toDataURL('image/png');
                    const pdf = new jspdf.jsPDF();

                    const imgProps= pdf.getImageProperties(imgData);
                    const pdfWidth = pdf.internal.pageSize.getWidth();
                    const pdfHeight = (imgProps.height * pdfWidth) / imgProps.width;
                    pdf.addImage(imgData, 'PNG', 0, 0, pdfWidth, pdfHeight);
                    
                   
                    pdf.save("Evrak.pdf");

                    // Kullanımdan sonra div'i kaldır
                    document.body.removeChild(div);
                });
            });
    } else {
    
        console.log('PDF indirme işlemi iptal edildi.');
    }
}