document.addEventListener('DOMContentLoaded', function () {
  $('#add_item').click(function () {
    $('.my_list').append('<li>Item</li>');
  });

  $('#remove_item').click(function () {
    $('li:last-of-type').remove();
  });

  $('#clear_list').click(function () {
    $('ul').empty();
  });
});
