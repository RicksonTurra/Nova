document.addEventListener('DOMContentLoaded', function() {
    token = document.getElementById("token")
    tokenData = token.innerHTML
    console.log(tokenData)
    fetch(`/status/response/${tokenData}`)
    .then(response => response.json())
    .then(response => {
        console.log(response)
        document.getElementById("status").innerHTML = response.status
    })
});