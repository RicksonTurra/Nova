document.addEventListener('DOMContentLoaded', function() {
    token = document.getElementById("token")
    tokenData = token.innerHTML
    console.log(tokenData)
    fetch(`/status/response/${tokenData}`)
    .then(response => response.json())
    .then(response => {
        console.log(response)
        document.getElementById("status").innerHTML = response.status
        
        // enable button in case the ticket is still OK
        const btn = document.getElementById("redeem")
        console.log(response.status)
        if ("Ticket is OK" === response.status){
            btn.disabled = false;
        }
    });
    const btn = document.getElementById("redeem")
    btn.addEventListener('click', redeem)


    function redeem(){
        fetch('/emails', {
            method: 'POST',
            body: JSON.stringify({
                body: 'redeem'
            })
          })
    }

    


});