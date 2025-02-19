function $(elt) {
    return document.getElementById(elt)
}

$("provider").addEventListener("change", function (){
    
    fetch("/api/models/")
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

// document.getElementById("chat-form").addEventListener("click", async function (event) {
//     event.preventDefault();
//     console.log("CAll me")
//     let formData = new FormData();
//     let message = document.getElementById("message").value;
//     let fileInput = document.getElementById("file-input");

//     formData.append("message", message);
//     formData.append("sender", "User1");
    
//     if (fileInput.files.length > 0) {
//         formData.append("file", fileInput.files[0]);

//         let response = await fetch("/api/v1/chat/upload/", {
//             method: "POST",
//             body: formData
//         });

//         let data = await response.json();
//         let chatContainer = document.getElementById("chat-container");

//         let newMessage = document.createElement("p");
//         newMessage.innerHTML = `You: ${data.message}`;
        
//         if (data.file_url) {
//             let fileLink = document.createElement("a");
//             fileLink.href = data.file_url;
//             fileLink.textContent = "Download File";
//             fileLink.target = "_blank";
//             newMessage.appendChild(document.createElement("br"));
//             newMessage.appendChild(fileLink);
//         }

//         chatContainer.appendChild(newMessage);
//     }
//     else{
//         console.log("hehe   ")
//     }
// });
