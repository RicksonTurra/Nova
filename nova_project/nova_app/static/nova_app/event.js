document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("button_refresh").addEventListener('click', refreshButton);
    document.getElementById("add").addEventListener('click', addTicket)

});

function refreshButton(){
    const id_event = document.getElementById("id-event").innerHTML
    fetch(`refresh/${id_event}`)
    .then(response => response.json())
    .then(response => {
        console.log(response);
        document.getElementById("redeem-value").innerHTML = response
    });
}

function addTicket(){
    
}