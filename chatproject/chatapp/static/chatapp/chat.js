function $(elt) {
    return document.getElementById(elt)
}

$("provider").addEventListener("change", function (){
    
    fetch("/api/models")
    .then(response => response.json())
    .then(data => {
        data = data.filter(model => model.toLowerCase().startsWith(this.value.toLowerCase() + "/"));
        const modelDropdown = document.getElementById("model");
        modelDropdown.innerHTML = ""; 

        data.forEach(model => {
            let option = document.createElement("option");
            option.value = model.split("/")[1];
            option.textContent = `${model}`;
            modelDropdown.appendChild(option);
        });
     
    })
    .catch(error => console.error("Error fetching models:", error));

})


function sendChatRequest() {
    const provider = document.getElementById("provider").value;
    const model = document.getElementById("model").value;
    const prompt = document.getElementById("prompt").value;

    if (!provider || !model || !prompt) {
        alert("Please select a provider, model, and enter a prompt.");
        return;
    }
    console.log(JSON.stringify({ provider, model, prompt }))

    fetch("/api/v1/chat/completions/", { 
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ provider, model, prompt })
    })
    .then(response => response.json())
    .then(data => {
        const responseContainer = document.getElementById("response");
        
        if (data.response) {
            responseContainer.innerHTML = `<strong>Response:</strong> ${data.response}`;
        } else {
            responseContainer.innerHTML = `<strong>Error:</strong> ${data.error || "No response received."}`;
        }
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById("response").innerHTML = `<strong>Error:</strong> Failed to get response.`;
    });
}
