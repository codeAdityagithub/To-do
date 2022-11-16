      var delform = document.getElementById("delform")
      var delinput = document.getElementById('delinp')
      var updateform = document.getElementById("updateform")
      var updateind = document.getElementById("updateind")
      var updateval = document.getElementById("updateval")
      var saveform = document.getElementById("saveform")
      var saveinput = document.getElementById("saveind")


      function del(element){
        console.log(delinput)
        delinput.value = element.id
        delform.submit()
      }
      function save(element){
        element.parentNode.previousSibling.previousSibling.setAttribute('contenteditable' , 'false')
        element.style.display = 'none'

        updateind.value = element.id
        updateval.value = element.parentNode.previousSibling.previousSibling.innerText
        updateform.submit()
      }
      function update(element){
        element.parentNode.previousSibling.previousSibling.setAttribute('contenteditable' , 'true')
        element.parentNode.previousSibling.previousSibling.focus()
        element.nextSibling.nextSibling.style.display = 'block'
      }