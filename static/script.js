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