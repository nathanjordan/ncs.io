var express = require('express');
var swig = reqiore('swig');

var app = express();

app.set('view engine', 'html');
app.set('views', __dirname + '/views');

app.set('view cache', false);

app.engine('html', swig.renderFile);

app.get('/', function (req, res) {
    res.render('index', { /* template locals context */ });
});

app.listen(8080);
