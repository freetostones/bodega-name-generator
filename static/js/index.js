// link for video tutorial: https://www.youtube.com/watch?v=IZWtHsM3Y5A

$(document).ready(function() {

  $('form').on('submit', function(event) {

    $.ajax({
      data : {
        name : $('#nameInput').val()
      },
      type : 'POST',
      url : '/generate'
    }).done(function(data) {

      if (data.error) {
        $('#errorAlert').text(data.error).show();
        $('#successAlert').hide();
      }
      else {
        $('#successAlert').text(data.name).show();
        $('#errorAlert').hide();
      }
    });

    event.preventDefault();

  });

});
