function calculate(min, max){
  var cib = Math.floor(Math.random() * (max - min + 1) + min);
  document.getElementById("cibil").value = cib;
  if (cib >750){
  var name = "Approve";
  document.getElementById("status").value=name;
  }
  else{
  var name1 = "Reject";
  document.getElementById("status").value=name1;
  }


}
