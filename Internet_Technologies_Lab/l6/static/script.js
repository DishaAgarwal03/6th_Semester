// $(document).ready(function() {
//     $('#coverForm').submit(function(event) {
//       event.preventDefault();
  
//       // Get form values
//       var imageURL = $('#imageInput').val();
//       var bgColor = $('#backgroundColor').val();
//       var fontSize = $('#fontSize').val() + 'px';
//       var fontColor = $('#fontColor').val();
//       var message = $('#textInput').val();
  
//     //   Generate cover preview
//       var coverPreview = $('#previewContent');
//       coverPreview.empty();
  
//       // Create cover elements
//       var coverImage = $('<img>').attr('src', imageURL).css('width', '100%');
//       var coverText = $('<p>').text(message).css({
//         'font-size': fontSize,
//         'color': fontColor,
//         'margin-top': '10px'
//       });
  
//       // Apply background color
//       coverPreview.css('background-color', bgColor);
  
//       // Append elements to preview
//       coverPreview.append(coverImage);
//       coverPreview.append(coverText);
//     });
//   });
  

$(document).ready(function() {
    $('#coverForm').submit(function(event) {
      event.preventDefault();
  
      // Get form values
      var imageFile = $('#imageInput')[0].files[0];
      var bgColor = $('#backgroundColor').val();
      var fontSize = $('#fontSize').val() + 'px';
      var fontColor = $('#fontColor').val();
      var message = $('#textInput').val();
  
      // Read image file
      var reader = new FileReader();
      reader.onload = function(event) {
        var imageURL = event.target.result;
  
        // Generate cover preview
        var coverPreview = $('#previewContent');
        coverPreview.empty();
  
        // Create cover elements
        var coverImage = $('<img>').attr('src', imageURL).css('width', '100%');
        var coverText = $('<p>').text(message).css({
          'font-size': fontSize,
          'color': fontColor,
          'margin-top': '10px'
        });
  
        // Apply background color
        coverPreview.css('background-color', bgColor);
  
        // Append elements to preview
        coverPreview.append(coverImage);
        coverPreview.append(coverText);
      };
  
      // Read image file as data URL
      reader.readAsDataURL(imageFile);
    });
  });
  