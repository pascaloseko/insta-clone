// toggle the upload and overlay
// $('#upload-but').click(function() {
//       $('#upload-div').toggle()
//       $('.overlay').toggle()
//   })

$('.caption-but').click(function() {
      $('#caption-div').slideToggle(200, function() {
      })
})

$('.effect').each(function() {
$(this).click(function() {
      $('#caption-div').slideUp(200, function() {
      })    
})
})