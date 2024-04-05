document.addEventListener("DOMContentLoaded", ()=> {
    document.querySelector("#dog-form").addEventListener(submitDogForm)
    })

    function submitDogForm(event) {
        event.preventDefault()
        let dog_form = new FormData(document.querySelector("#dog-form"))

        fetch("/dogs/", {
            method: 'post',
            body: dog_form
        }).then(response => response.json()).then(data =>)
    }