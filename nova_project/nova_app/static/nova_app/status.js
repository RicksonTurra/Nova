document.addEventListener('DOMContentLoaded', function() {
    token = document.getElementById("token")
    tokenData = token.innerHTML
    console.log(tokenData)
    fetch(`/status/response/${tokenData}`)
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


    
    const bttn = document.getElementById("redeem")
    bttn.addEventListener('click', function(e){
        e.preventDefault();
        // Redeems the ticket
        tokenNew = document.getElementById("token")
        tokenDataNew = token.innerHTML
        fetch(`/redeem/${tokenDataNew}`)
        .then(response => response.json())
        .then(response => {
            console.log(response)
            fetch(`/status/response/${tokenData}`)
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
        
    });

});
    

    


