$('tr td').each(function(){
  if($(this).text() > 5)$(this).css('background-color','red');
});
