const updateClasses = function(elementName) {

    for (const element of document.querySelectorAll(`${elementName},input,textarea,select,option`)) {
    

        if (element.id === "id_date") {
  
            element.type = "date"
        }

        if (element.parentNode.id === 'id_type') {

            continue;
        }
  
        if (["id_plankareNo", 'id_noResult', 'id_secondaryNo'].includes(element.id)) {
  
            element.setAttribute('readonly', 'true')
        }


        if (['id_area'].includes(element.id)) {

            element.classList.add('d-flex', 'flex-wrap', 'mb-3')
            element.style.gap = '20px'
            continue;
        }

        if (element.type === 'checkbox' && ['area', 'type'].includes(element.name)) {

            element.classList.add('form-check-input')
            continue;
        }
  
        element.classList.add('form-control')
        element.classList.add('mb-3')
    }
}

window.onload = function() {

   // trigger
   updateClasses('#submit-buluntu')
   updateClasses('#id_area')

  // plankare starts
  const plankareX = document.getElementById('id_plankareX')
  const plankareY = document.getElementById('id_plankareY')
  const plankareNo = document.getElementById('id_plankareNo')

  // buluntu alanı
  const buluntuNo = document.getElementById('id_no')
  const buluntuNoSonuc = document.getElementById('id_noResult')
  const kucukBuluntuNo = document.getElementById('id_secondaryNo')
  const buluntuTur = document.querySelector("#genel-buluntu #id_type")

 let flag = "";

  const set_value_for_input = function(action) {
    
      let displayValue = `${plankareX.value} ${plankareY.value}` || "";

      if (buluntuNo.value) {
          displayValue = `${plankareX.value} ${plankareY.value}-${buluntuNo.value}`
      }



      const option = buluntuTur.value.toLowerCase()

      switch(action) {

          case "plankareX":
          case "plankareY":
          plankareNo.value = `${plankareX.value} ${plankareY.value}`
          break;
          
      }


      // selected option loop atilacak

      flag = ""
      const selectedOptions = Array.from(buluntuTur.selectedOptions).map(option => option.value.toLowerCase())
      for (const option of selectedOptions) {

    
        if (option == "küçük buluntu") {

            kucukBuluntuNo.removeAttribute('readonly')
            flag = "/"
            
            if (!buluntuNo.value) { buluntuNo.focus()}
            else if (!kucukBuluntuNo.value) {kucukBuluntuNo.focus()}
            continue
        }

        if (option == "taş") {

            flag += ",c"
            continue
        
        }


        if (option == "kemik") {

            flag += ",b"
        }


      }

      if (!flag.includes('/')) {

        kucukBuluntuNo.value = ""
        kucukBuluntuNo.setAttribute('readonly', 'true')
      }

      if (flag.length && option == "küçük buluntu") {

          displayValue = `${plankareX.value} ${plankareY.value}-${buluntuNo.value} ${flag} ${kucukBuluntuNo.value}`
          
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

  //buluntu türü dropdown
  buluntuTur.addEventListener('change', function (e) {

      set_value_for_input("buluntuTur")
  })


 // end of plankare


   // color_field
   const colorDropdown = document.getElementById('id_colour')
   const colorPreview = document.getElementById('id_palet')  

   colorPreview.setAttribute('disabled', 'true')
   colorDropdown.onchange = function(event) {

          colorPreview.value = event.target.value;
   }

 

// dropdown change
document.getElementById('id_buluntuForms').addEventListener('change', async function () {
    // Seçilen seçeneği al
    let selectedOption = this.value;
    const api = await fetch(`http://127.0.0.1:8000/buluntu/forms/${selectedOption}`)
    const api_response = await api.text()

    console.log("TEST APİ:", api_response)

    if (selectedOption) {
        const modalId = "#buluntu-modal";

        const targetContainer = document.getElementById('ek-modal')
        targetContainer.innerHTML = api_response;

        const heading = document.getElementById(`target-buluntu`)
        heading.innerText += ` (${buluntuNoSonuc.value})`

        updateClasses("ek-modal")

        const modal = new bootstrap.Modal(document.querySelector(modalId));
        modal.show();


    }
});





}