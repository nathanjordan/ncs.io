var express = require('express');
var swig = require('swig');
var path = require('path');

var app = express();

app.set('view engine', 'html');
app.set('views', path.resolve(__dirname, '../', 'views'));

app.set('view cache', false);

app.engine('html', swig.renderFile);

app.use(express.static(path.resolve(__dirname, '../static')));

app.get('/', function (req, res) {
    res.render('index', { });
});

app.listen(8080);
