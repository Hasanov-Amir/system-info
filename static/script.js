// list of all buttons
const buttons = document.querySelectorAll('button');
// start dir input
const inputdiv = document.getElementById("start");
// start input
const input = document.getElementById("dir");
// getting domain name
const domain = window.location.href;
console.log(inputdiv)

// listening for click on buttons
buttons.forEach(button => {
    button.addEventListener('click', () => {
        // run function for getting util response
        if (button.id === "empty_dirs") {
            inputdiv.style.visibility = 'visible';
            checkInput(button.id);
        } else {
            GetResponse(button.id);
        }
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


function checkInput(button) {
    if (input.value) {
        GetResponse(button)
    }
}
