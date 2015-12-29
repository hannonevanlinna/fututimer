var cool = require('cool-ascii-faces');
var express = require('express');
var app = express();

  var fs = require('fs');
var http = require('http');
var url = require('url') ;


var timestart = new Date;
var hour = timestart.getHours();
var minute = timestart.getMinutes();
var milliseconds = timestart.getMilliseconds();
var timeraika = 10;
var timerrunning = 0;


app.set('port', (process.env.PORT || 5000));

app.use(express.static(__dirname + '/public'));

// views is directory for all template files
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');



app.get('/parametri', function(request, response) {

  var queryObject = url.parse(request.url,true).query;
  var uusiaika = queryObject.time

  response.writeHead(200, {"Content-Type": "text/plain"});
  //response.end("parametri" +JSON.stringify(queryObject));
  timeraika = uusiaika;
response.end("parametri" +uusiaika);
});


//alustaa timerin
app.get('/timerstart', function(request, response) {	
  timestart = new Date;
  timerrunning = 1;
  response.writeHead(200, {"Content-Type": "text/plain"});
  response.end("Count down running" + timeraika);

});  




app.get('/time', function(request, response) {
  if (timerrunning){
	  var timenow = new Date;
	  var timedifference = (timestart - timenow + 1000*timeraika)/1000;
	  if (timedifference>0) {
		  response.writeHead(200, {"Content-Type": "text/plain"});
	  	  response.end('Time left: ' + timedifference);
		}
		else {
			timerruning = 0;
			response.writeHead(200, {"Content-Type": "text/plain"});
  			response.end('timer stopper.' + timeraika);
		}

	}
	else {
	response.writeHead(200, {"Content-Type": "text/plain"});
  	response.end('timer stopper.' + timeraika);

	}
});

//app.get('/settimer', function(request, response) {
//  timestart = new Date;
//  response.writeHead(200, {"Content-Type": "text/plain"});
//  response.end("Aika asetettu");
//});

//app.get('/seconds', function(request, response) {
//  var timenow = new Date();
  //var timedifference = (timenow - timestart)/1000;
   
  //response.writeHead(200, {"Content-Type": "text/plain"});
  //response.end('processtime' + timedifference);
//});

//app.get('/minutes', function(request, response) {
  //var timenow = new Date;
  //var timedifference = timenow.getMinutes() - timestart.getMinutes();

  //response.writeHead(200, {"Content-Type": "text/plain"});
//  response.end('minute' + timedifference);
//});

//app.get('/cool', function(request, response) {
 // response.send(cool());
//});

//app.get('/', function(request, response) {
//  var result = ''
  //var times = process.env.TIMES || 50
  //for (i=0; i < times; i++)
    //result += cool();
  //response.send(result);
//});

//app.get('/20', function(request, response) {
  //var result = ''
  //var times = process.env.TIMES || 20
  //for (i=0; i < 20; i++)
  // result += cool();
  //response.send(result);
//});

//app.get('/hello', function(request, response) {
//  response.writeHead(200, {"Content-Type": "text/plain"});
//  response.end("Hello World\n");
//});

app.listen(app.get('port'), function() {
  console.log('Node app is running on port', app.get('port'));
});


