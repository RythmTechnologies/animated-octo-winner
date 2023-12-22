window.onload = function () {

    document.querySelectorAll('#submit-buluntu,input,textarea,select,option').forEach(function (element) {

        if (element.id === "id_date") {

            element.type = "date"
        }

        if (["id_plankareNo", 'id_noResult'].includes(element.id)) {

            element.disabled = true
        }

        element.classList.add('form-control')
        element.classList.add('mb-3')
    })


    // plankareler alanı
    const plankareX = document.getElementById('id_plankareX')
    const plankareY = document.getElementById('id_plankareY')
    const plankareNo = document.getElementById('id_plankareNo')

    // buluntu alanı
    const buluntuNo = document.getElementById('id_no')
    const buluntuNoSonuc = document.getElementById('id_noResult')
    const kucukBuluntuNo = document.getElementById('id_secondaryNo')
    const buluntuTur = document.getElementById('id_type')

    if (plankareX) {
        plankareX.addEventListener("change", function (e) {

            let output = `${e.target.value} ${plankareY.value}`
            let buluntuNoOutput;

            plankareNo.value = output

            buluntuNoOutput = `${output} ${buluntuNo.value} / `

            if (kucukBuluntuNo.value) {
                buluntuNoOutput += kucukBuluntuNo.value
            }

            buluntuNoSonuc.value = buluntuNoOutput
        })
    }

    if (plankareY) {
        plankareY.addEventListener("change", function (e) {


            let output = `${plankareX.value} ${e.target.value}`
            let buluntuNoOutput;


            plankareNo.value = output

            buluntuNoOutput = `${output} ${buluntuNo.value} / `

            if (kucukBuluntuNo.value) {
                buluntuNoOutput += kucukBuluntuNo.value
            }

            buluntuNoSonuc.value = buluntuNoOutput

        })
    }





    // plankareler alanı biter

    if (buluntuNo) {
        buluntuNo.addEventListener('change', function (e) {

            buluntuNoSonuc.value = `${plankareX.value} ${plankareY.value}  ${e.target.value} /`
        })
    }


    if (kucukBuluntuNo) {
        kucukBuluntuNo.addEventListener('change', function (e) {

            buluntuNoSonuc.value = `${plankareX.value} ${plankareY.value} ${buluntuNo.value} / ${e.target.value}`

        })
    }



    if (buluntuTur) {
        buluntuTur.addEventListener('change', function (e) {
            console.log("event buluntu tur:", e.target.value.toLowerCase())
            let output;
            switch (e.target.value.toLowerCase()) {

                case "keramik":
                case "küçük buluntu":

                    output = `${plankareX.value} ${plankareY.value} ${buluntuNo.value} / ${kucukBuluntuNo.value}`
                    break;

                case "kemik":
                    output = `${plankareX.value} ${plankareY.value} ${buluntuNo.value}b / ${kucukBuluntuNo.value}`
                    break;

                case "taş":
                    output = `${plankareX.value} ${plankareY.value} ${buluntuNo.value}c / ${kucukBuluntuNo.value}`
                    break;

            }

            buluntuNoSonuc.value = output

        })
    }


    // preview
    const create_preview_element = function(id) {

        const element = document.createElement("img")
        element.style.width = "100%"

        element.id = `preview-${id}`

        return element
      }
      
      
      const update_preview_image = function(targetId, meta) {
      
        const reader = new FileReader();

        reader.onload = function (e) {
            document.querySelector(`#preview-${targetId}`).setAttribute("src", e.target.result)
        };

        reader.readAsDataURL(meta);
      }
      
   


      document.querySelectorAll('#imageElements input').forEach(function(element) {
        
            if (element.type === 'file' && element.id.includes("id_type")) { 

            const previewElement = create_preview_element(element.id)
            const clearElement = document.createElement('input')

            element.onchange = function(event) {
                update_preview_image(element.id, event.target.files[0])
                clearElement.style.display = "block"
            }

            element.insertAdjacentElement("afterend", previewElement)


            clearElement.style.display = "none"
            clearElement.type = 'button'
            clearElement.value = "Temizle"
            clearElement.id = `clear-preview-${element.id}`
            
            clearElement.onclick = function() {
                element.value = ""
                previewElement.src = ""
                clearElement.style.display = "none"
            }

            element.insertAdjacentElement("afterend", clearElement)
        } 
      })
  
}
