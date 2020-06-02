
window.onmessage = function(e) {
  if (e.data=="hideiframe") {
    document.getElementById('id_feedback_container').className='hidden';
  }
}

function showDialog() {
  document.getElementById('id_feedback_container').className='';
  window.frames[0].postMessage("showdialog", "https://www.pythonanywhere.com");
  return false;
}


