
window.onmessage = function(e) {
  if (e.data=="hideiframe") {
    document.getElementById('id_feedback_container').className='hidden';
  }
}

function showDialog() {
  console.log("showing dialog");
  document.getElementById('id_feedback_container').className='';
  window.frames[0].postMessage("showdialog", "https://www.pythonanywhere.com");
  return false;
}

$(document).ready(function() {
  console.log("attaching event");
  $("#id_feedback_link").click(function() {
    showDialog();
  });
});

