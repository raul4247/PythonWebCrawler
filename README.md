# PythonWebCrawler
A Simple Python Web Crawler

## Types of references that are currently being filtered:
* starts with one back slash '/'
   e.g: '/home/login.php'

* starts with two bslashes '//'
   e.g:  '//www<!-- -->.youtube.com/upload'

* starts with a dot slash './'
   e.g: './about.php'
* starts with a anchor '#'
   e.g: '#sectionB'

* starts with two dots and slash '../'
   e.g: '../link.html'

* javascript links
   e.g: javascript:d
  

* missing scheme and host on url
   e.g: 'page.php'

* already fine reference
   e.g: https<!-- -->://www.google.com/