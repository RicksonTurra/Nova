document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#index-view').style.display = 'none';
    document.getElementById("check").addEventListener('keypress', function(e){
        if (e.key === 'Enter') {
            status(e)
          }
    })
    const bttn = document.getElementById("redeem")
    bttn.addEventListener('click', function(e){
        redeem(e)
        
    });

})


function status(e){
    e.preventDefault();
    content = document.getElementById("check").value;
    fetch(`/status/response/${content}`)
    .then(response => response.json())
    .then(response => {
        // console.log(response)
        document.getElementById("status").innerHTML = response.status
        document.querySelector('#index-view').style.display = 'block';
        // enable button in case the ticket is still OK
        const btn = document.getElementById("redeem")
        console.log(response.status)
        if ("Ticket is OK" === response.status){
            btn.disabled = false;
        }
    }); 
}

function redeem(e){
    e.preventDefault();
// Redeems the ticket
content = document.getElementById("check").value;
fetch(`/redeem/${content}`)
.then(response => response.json())
.then(response => {
    console.log(response)
    fetch(`/status/response/${content}`)
    .then(response => response.json())
    .then(response => {
    // console.log(response)
    document.getElementById("status").innerHTML = response.status

    // enable button in case the ticket is still OK
    const btn = document.getElementById("redeem")
    // console.log(response.status)
    if ("Ticket is OK" === response.status){
        btn.disabled = false;
        }
    });
})
}
