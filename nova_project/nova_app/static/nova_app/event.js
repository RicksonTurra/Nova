document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("button_refresh").addEventListener('click', refreshButton);
    document.getElementById("tickets-form").addEventListener('submit', function(e){
        const id_event = document.getElementById("id-event").innerHTML;
        const numberTickets = document.getElementById("tickets").value;
        console.log(numberTickets)
        fetch('/add', {
            method: 'POST',
            body: JSON.stringify({
                pkid: `${id_event}`,
                number: `${numberTickets}`,
            })
          })    
        });

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
