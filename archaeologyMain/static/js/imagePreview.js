const create_preview_element = function(id) {

    const previewElement = document.createElement("img")

    previewElement.style.width = "100%";
    previewElement.style.maxWidth = "200" + "px";
    previewElement.style.height = "200" + "px";
    previewElement.style.maxHeight = "200" + "px";
    previewElement.style.objectFit = "cover";

    previewElement.id = `preview-${id}`

    return previewElement
  }


  const create_clear_element = function(element, previewElement) {

    const clearElement = document.createElement("input")
    
    clearElement.style.display = "none"
    clearElement.type = 'button'
    clearElement.value = "Temizle"
    clearElement.id = `clear-preview-${element.id}`
    
    clearElement.onclick = function() {
        element.value = ""
        previewElement.removeAttribute('src')
        clearElement.style.display = "none"
    }


    return clearElement
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
    const clearElement = create_clear_element(element, previewElement)

    element.onchange = function(event) {
        update_preview_image(element.id, event.target.files[0])
        clearElement.style.display = "block"
    }

    element.insertAdjacentElement("afterend", previewElement)
    element.insertAdjacentElement("afterend", clearElement)
} 
})