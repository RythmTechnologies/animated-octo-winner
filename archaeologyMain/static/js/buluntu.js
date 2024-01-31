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
  const buluntuTur = document.querySelector("#genel-buluntu #id_type")

  let flag = "";

  const set_value_for_input = function(action) {
    



      let displayValue = `${plankareX.value} ${plankareY.value}` || "";

      if (buluntuNo.value) {
          displayValue = `${plankareX.value} ${plankareY.value} ${buluntuNo.value}`
      }



      const option = buluntuTur.value.toLowerCase()
      console.log("OPTİOOOON:", option)

      switch(action) {

          case "plankareX":
          case "plankareY":
          plankareNo.value = `${plankareX.value} ${plankareY.value}`
          break;

          case "buluntuTur":
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

  //buluntu türü dropdown
  buluntuTur.addEventListener('change', function (e) {

      set_value_for_input("buluntuTur")
  })


 // end of plankare


   // color_field
   const colorDropdown = document.getElementById('id_colour')
   const colorPreview = document.getElementById('id_palet')  

   colorDropdown.onchange = function(event) {

          colorPreview.value = event.target.value;
   }

 

// dropdown change
document.getElementById('id_buluntuForms').addEventListener('change', function () {
    // Seçilen seçeneği al
    let selectedOption = this.value;

    if (selectedOption) {
        const heading = document.getElementById(`target-buluntu-${selectedOption}`)
        heading.innerText += ` (${buluntuNoSonuc.value})`
        const modalId = '#buluntu-' + selectedOption;
        const modal = new bootstrap.Modal(document.querySelector(modalId));
        modal.show();
    }
});

}