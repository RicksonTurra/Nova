document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('#index-view').style.display = 'none';
    document.getElementById("check").addEventListener('submit', function(e){
        status()
    }

}


function status(){
    e.preventDefault();
    const content = document.getElementById("ticket").value;
    fetch(`/status/response/$`{content}`)
    .then(response => response.json())
    .then(response => {
        // console.log(response)
        document.getElementById("status").innerHTML = response.status
        document.querySelector('#index-view').style.display = 'block';
        // enable button in case the ticket is still OK
        const btn = document.getElementById("redeem")
        // console.log(response.status)
        if ("Ticket is OK" === response.status){
            btn.disabled = false;
        }
    }); 
}