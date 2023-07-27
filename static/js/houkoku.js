function setTodayDate() {
    var today = new Date();
    var day = today.getDate();
    var month = today.getMonth() + 1;
    var year = today.getFullYear();

    var dateField = document.getElementById('date');
    dateField.value = year + '-' + addLeadingZero(month) + '-' + addLeadingZero(day);
  }

  function addLeadingZero(number) {
    return ('0' + number).slice(-2);
  }

  function selectAttendanceButton(button) {
    var buttons = document.querySelectorAll('.attendance-button');
    buttons.forEach(function(btn) {
      btn.classList.remove('active');
    });
    button.classList.add('active');
  }
  

  function confirmSubmission() {
    var result = confirm("送信しますか？");
    
    if (result) {

      alert("送信しました！");
    } else {
  
      alert("キャンセルしました。");
    }
  }



  const textarea = document.getElementById('textarea');
  const btn = document.getElementById('btn');

  textarea.addEventListener('keyup', (e) => {
    if (e.target.value.length > 30) {
      alert("1000文字以内で記述してください。");
      btn.disabled = true;
    };
    if (e.target.value.length <= 1000) {
      btn.disabled = false;
    };
  });



  var formData = new FormData();
  formData.append('username', 'John');
  formData.append('password', 'password123');


  var request = new XMLHttpRequest();
  request.open('POST', 'https://example.com/api/endpoint');
  request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');


  request.onload = function() {
  if (request.status === 200) {
    console.log(request.responseText);
  } else {
    console.error('リクエストエラー:', request.status);
  }
};

request.send(formData);