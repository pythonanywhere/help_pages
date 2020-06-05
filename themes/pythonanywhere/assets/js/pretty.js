$('a.image-reference:not(.islink) img:not(.islink)').parent().colorbox(
  {rel:"gal",maxWidth:"100%",maxHeight:"100%",scalePhotos:true}
);
moment.locale("${momentjs_locales[lang]}");
fancydates(${date_fanciness}, ${js_date_format});

