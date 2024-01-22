const create_preview_element = function(id) {

    const element = document.createElement("img")
    element.style.width = "100%";
    element.style.maxWidth = "200" + "px";
    element.style.maxHeight = "200" + "px";
    element.style.objectFit = "cover";

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
      
    if (element.type === 'file' && element.id.startsWith("id")) { 

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