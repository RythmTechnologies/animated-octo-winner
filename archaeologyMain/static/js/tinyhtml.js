tinyMCE.init({
  mode: "textareas",
  theme: "silver",
  plugins: "spellchecker,directionality,paste,searchreplace",
  language: "tr",
  branding: false,
  directionality: "{{ directionality }}",
  spellchecker_languages : "{{ spellchecker_languages }}",
  spellchecker_rpc_url : "{{ spellchecker_rpc_url }}",
  skin: (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'oxide-dark' : 'oxide'),
  content_css: (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'default'),
  menubar: false
});
