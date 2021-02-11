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
    // console.log(response);
    response = JSON.parse(response);
    response.forEach(show_events);
    });    
}
    
function show_events(all_events){
    console.log(all_events.fields['name_field']);
    // Create name variable 
    const name = all_events.fields['name_field'];

    // Create div for name
    const name_div = document.createElement('div');
    const name_span = document.createElement('span');
    // Set attributes to name_span
    name_span.className = 'eventName'
    name_span.innerHTML = `Event: ${name}`
    name_div.appendChild(name_span);
    

    // Create button to check event
    const event_button = document.createElement('button');
    // Set attributes to button
    // event_button.setAttribute('type', 'submit');
    event_button.setAttribute('value', 'Check');
    event_button.setAttribute('id', 'check');
    event_button.className = 'btn btn-primary btn-lg'
    name_span.appendChild(event_button);

    // Add div to DOM
    document.querySelector('#events-view').append(name_div);
    
}
// document.getElementById('check').addEventListener('click', `load_id(${name})`);
event_button.setAttribute('onclick', `load_id(${name})`);
function load_id(){
    console.log('ola')
    console.log(`${name}`);
    window.location.replace(`/event`);
}