function inputInt(x){
    document.getElementById("input").value += x;
}
function sbros(){
    document.getElementById("input").value = "";
}
function dl(){
   a =  document.getElementById("input").value
   document.getElementById("input").value = a.slice(0, -1) 
}
function delIncorrect(){
    if (document.getElementById("input").value == "incorrect"){
        document.getElementById("input").value = ""
    } 
}

async function calc(e) {
    e.preventDefault();
    const input = document.getElementById('input');
    const response = await fetch('/api/calc/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json;charset=utf-8'
        },
        body: JSON.stringify({expression: input.value})
    });
    const result = await response.json();
    input.placeholder = result.placeholder;
    input.value = result.value;
}