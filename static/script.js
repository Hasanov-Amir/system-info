const buttons = document.querySelectorAll('button');

buttons.forEach(button => {
    button.addEventListener('click', () => {
        GetResponse(button.id);
    });
});


function GetResponse (name) {
    const url = `http://127.0.0.1:5000/${name}`;
    const outputDiv = document.getElementById('output');
    outputDiv.textContent = "";

    fetch(url)
        .then(response => response.json())
        .then(data => {
            data.res.forEach(line => {
                outputDiv.textContent += `${line}\n`;
            })
        })
        .catch(error => {
            console.log(error);
        });
}