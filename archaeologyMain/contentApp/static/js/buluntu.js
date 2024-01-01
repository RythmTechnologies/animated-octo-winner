window.onload = function() {

    document.querySelectorAll('#submit-buluntu,input,textarea,select,option').forEach(function (element) {

        if (element.id === "id_date") {

            element.type = "date"
        }

        if (["id_plankareNo", 'id_noResult', 'id_secondaryNo'].includes(element.id)) {

            element.disabled = true
        }

        element.classList.add('form-control')
        element.classList.add('mb-3')
    })


    // plankare starts
    const plankareX = document.getElementById('id_plankareX')
    const plankareY = document.getElementById('id_plankareY')
    const plankareNo = document.getElementById('id_plankareNo')

    // buluntu alanı
    const buluntuNo = document.getElementById('id_no')
    const buluntuNoSonuc = document.getElementById('id_noResult')
    const kucukBuluntuNo = document.getElementById('id_secondaryNo')
    const buluntuTur = document.getElementById('id_type')

    let flag = "";

    const set_value_for_input = function(action) {

        let displayValue = `${plankareX.value} ${plankareY.value}` || "";

        if (buluntuNo.value) {
            displayValue = `${plankareX.value} ${plankareY.value} ${buluntuNo.value}`
        }



        const option = buluntuTur.value.toLowerCase()
  

        switch(action) {

            case "plankareX":
            case "plankareY":
            plankareNo.value = `${plankareX.value} ${plankareY.value}`
            break;

            case "bulunuTur":
            // reset
            if (option == "küçük buluntu") {

                kucukBuluntuNo.disabled = false
                flag = "/"
                
                if (!buluntuNo.value) { buluntuNo.focus()}
                else if (!kucukBuluntuNo.value) {kucukBuluntuNo.focus()}

            } else {
                kucukBuluntuNo.disabled = true
                flag = ""
            } 
            
            if (option == "taş") {

                flag = "c"
            }

            if (option == "kemik") {

                flag = "b"
            } 

        }


        if (flag.length && option == "küçük buluntu") {

            displayValue = `${plankareX.value} ${plankareY.value} ${buluntuNo.value} ${flag} ${kucukBuluntuNo.value}`
            
        } else if (flag.length) {

            displayValue = `${displayValue}${flag}`
        }

        buluntuNoSonuc.value = displayValue
    }

    // set values for first time
    set_value_for_input("plankareX")

    plankareX.addEventListener("change", function (e) {


        set_value_for_input("plankareX")

    })


    plankareY.addEventListener("change", function (e) {

        set_value_for_input("plankareY")
    })


    // buluntu no sonuç
    buluntuNo.addEventListener('change', function (e) {

        set_value_for_input()

        if (!kucukBuluntuNo.value) {kucukBuluntuNo.focus()}
    })


    // küçük buluntu no sonuç
    kucukBuluntuNo.addEventListener('change', function (e) {

        set_value_for_input()

        if (!buluntuNo.value) {kucukBuluntuNo.focus()}
    })

    // buluntu türü dropdown
    buluntuTur.addEventListener('change', function (e) {

        set_value_for_input("bulunuTur")
    })


   // end of plankare


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
      



     // color_field
     const colorDropdown = document.getElementById('id_colour')
     const colorPreview = document.getElementById('id_palet')  

     colorDropdown.onchange = function(event) {

            colorPreview.value = event.target.value;
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