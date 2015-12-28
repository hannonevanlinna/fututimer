var cool = require('cool-ascii-faces');
var express = require('express');
var app = express();

app.set('port', (process.env.PORT || 5000));

app.use(express.static(__dirname + '/public'));

// views is directory for all template files
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');

app.get('/', function(request, response) {
  var result = ''
  var times = process.env.TIMES || 50
  for (i=0; i < times; i++)
    result += cool();
  response.send(result);
});

app.get('/2', function(request, response) {
  var result = ''
  var times = process.env.TIMES || 2
  for (i=0; i < times; i++)
    result += cool();
  response.send(result);
});

app.get('/hello', function(request, response) {
  response.writeHead(200, {"Content-Type": "text/plain"});
  response.end("Hello World\n");
});

app.get('/cool', function(request, response) {
  response.send(cool());
});

app.listen(app.get('port'), function() {
  console.log('Node app is running on port', app.get('port'));
});


