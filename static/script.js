// list of all buttons
const buttons = document.querySelectorAll('button');
// getting domain name
const domain = window.location.href;


// listening for click on buttons
buttons.forEach(button => {
    button.addEventListener('click', () => {
        // run function for getting util response
        GetResponse(button.id);
    });
});


function GetResponse (name) {
    const url = `${domain}${name}`;
    const resDiv = document.getElementById('output');
    resDiv.textContent = "";

    // requesting to utils url
    fetch(url)
        .then(response => response.json())
        .then(data => {
            // writing response
            data.res.forEach(line => {
                resDiv.textContent += `${line}\n`;
            })
        })
        .catch(error => {
            console.log(error);
        });
}
