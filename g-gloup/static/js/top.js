function selectAttendanceButton(button) {
    var buttons = document.querySelectorAll('.attendance-button');
    buttons.forEach(function(btn) {
      btn.classList.remove('active');
    });
    button.classList.add('active');
  }