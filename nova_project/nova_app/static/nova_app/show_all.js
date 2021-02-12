document.addEventListener('DOMContentLoaded', function() {
     load_events();
});


function load_events(){
    //Get data - API
    fetch('/show')
    .catch(error => {
    console.log('Error: ', error)
    })
    .then(response => response.json())
    .then(response => {
    console.log(response);
    response = JSON.parse(response);
    response.forEach(show_events);
    });    
}
    
function show_events(all_events){
    console.log(all_events.fields['name_field']);
    console.log(all_events.pk)
    // Create name variable 
    const name = all_events.fields['name_field'];
    const idName= all_events.pk
    // Create div for name
    const name_div = document.createElement('tr');
    const name_span = document.createElement('td');
    const name_span1 = document.createElement('td');
    // Set attributes to name_span
    name_span.className = 'eventName'
    name_span.innerHTML = `Event: ${name}`
    name_div.appendChild(name_span);
    name_div.appendChild(name_span1);
    

    // Create button to check event
    const event_button = document.createElement('input');
    // Set attributes to button
    // event_button.setAttribute('type', 'submit');
    event_button.setAttribute('value', 'Check');
    event_button.setAttribute('id', '${idName}');
    event_button.className = 'btn btn-primary';
    name_span1.appendChild(event_button);
    event_button.addEventListener("click", () => load_id(`${idName}`));

    // Add div to DOM
    document.querySelector('#events-view').append(name_div);
    
}
// document.getElementById('check').addEventListener('click', `load_id(${name})`);
function load_id(idName){
    window.location.replace(`/event/${idName}`);
}