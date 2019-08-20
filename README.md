# stock_sim

## Project setup
Installations: 
* Node.JS 
* PHP 
* Laragon/ XAMPP 

Frameworks
```
npm install @vue/cli
composer require laravel/passport
```

### Launching the Servers
1. Run client-side server by using the command below on cmd:
```
cd \root\ --> Must be in the root folder of the repo!!
npm run serve
```
2. Run the database by using either Laragon/ XAMPP.
3. Run server-side by using the command below on cmd:
```
cd \auth\ --> cd into the auth folder.
php artisan serve
```
### When getting CORS Error upon logging in.
On Windows Run (Windows Key + R), copy and paste the following code.
```
chrome.exe --user-data-dir="C:/Chrome dev session" --disable-web-security
```

### Compiles and minifies for production
```
npm run build
```

### Run your tests
```
npm run test
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
