document.addEventListener('DOMContentLoaded', function() {
    document.getElementById("button_refresh").addEventListener('click', refreshButton);
});

function refreshButton(){
    const name_event = document.getElementById("event_name").innerHTML
    console.log(name_event)
    fetch(`refresh/${name_event}`)
    .then(response => response.json())
    .then(response => {
        console.log(response);
        document.getElementById("redeem-value").innerHTML = response
    });
}