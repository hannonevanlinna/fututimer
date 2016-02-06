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
var timeraika = 600;
var timerrunning = 0;
var timedifference = timeraika; 
var changedate = new Date;
var message = "";

app.set('port', (process.env.PORT || 5000));
app.use(express.static(__dirname + '/public'));

// views is directory for all template files
app.set('views', __dirname + '/views');
app.set('view engine', 'ejs');
app.get('/', function(req, res) {
    res.render('pages/index');
});


app.get('/parametri', function(request, response) {

  var queryObject = url.parse(request.url,true).query;
  var uusiaika = queryObject.time

  response.writeHead(200, {"Content-Type": "text/plain"});
  //response.end("parametri" +JSON.stringify(queryObject));
  timerrunning = 1;
  timeraika = uusiaika;
  changedate = new Date;
  response.end("parametri" +uusiaika);
});

app.get('/settext', function(request, response) {

  var queryObject = url.parse(request.url,true).query;
  message = queryObject.message

  response.writeHead(200, {"Content-Type": "text/plain"});
  //response.end("parametri" +JSON.stringify(queryObject));
  changedate = new Date;
  response.end("message" +message);
});


app.get("/api/status", function(request, response) {

	if (timerrunning == 2){
	  var timenow = new Date;
	  timedifference = (timestart - timenow + 1000*timeraika)/1000;
	  if (timedifference>0) {
	  	var timedifferencekokonais = timedifference.toFixed();
	  	response.writeHead(200, {"Content-Type": "application/json"});
		response.end(JSON.stringify({"status": timerrunning, "time": timeraika, "timeleft": timedifferencekokonais, "message": message, "changedate": changedate}));
		}
		else {
			timerruning = 2;
	  		response.writeHead(200, {"Content-Type": "application/json"});
			response.end(JSON.stringify({"status": timerrunning, "time": timeraika, "timeleft": "0", "message": message, "changedate": changedate}));

		}
	if (timedifference < -10){
		timerrunning = 0;
		changedate = new Date;


	}


	}
	else {

	response.writeHead(200, {"Content-Type": "application/json"});
	response.end(JSON.stringify({"status": timerrunning, "time": timeraika, "timeleft": "0", "message": message, "changedate": changedate}));

	}

	
});

app.get('/status', function(request, response) {	
  response.writeHead(200, {"Content-Type": "text/plain"});
  response.end("" +timerrunning);

}); 

app.get('/message', function(request, response) {	
  response.writeHead(200, {"Content-Type": "text/plain"});
  response.end("" +message);

}); 


//käynnistää timerin
app.get('/timerstart', function(request, response) {	
  timestart = new Date;
  changedate = new Date;
  timerrunning = 2;
  response.writeHead(200, {"Content-Type": "text/plain"});
  response.end("Count down running" + timeraika);
});  



//valmistelee timerin, muuttaa changedaten.
app.get('/getready', function(request, response) {	
  timerrunning = 1;
  changedate = new Date;
  response.writeHead(200, {"Content-Type": "text/plain"});
  response.end("Count down waiting to start" + timeraika);

});  

//Pause
app.get('/pause', function(request, response) {	
  timerrunning = 1;
  changedate = new Date;
  var timeraikakokonais = timedifference.toFixed();
  timeraika = timeraikakokonais;
  response.writeHead(200, {"Content-Type": "text/plain"});
  response.end("Count down waiting to start" + timeraika);

});  

app.get('/time', function(request, response) {
  if (timerrunning == 2){
	  var timenow = new Date;
	  timedifference = (timestart - timenow + 1000*timeraika)/1000;
	  if (timedifference>0) {
	  	var timedifferencekokonais = timedifference.toFixed();
		  response.writeHead(200, {"Content-Type": "text/plain"});
	  	  response.end('' +timedifferencekokonais);
		}
		else {
			timerruning = 2;
			response.writeHead(200, {"Content-Type": "text/plain"});
  			response.end('' + 0);
		}

	}
	else {

	response.writeHead(200, {"Content-Type": "text/plain"});
  	response.end('' + timeraika);

	}
});

//käynnistää timerin
app.get('/showtime', function(request, response) {	
  timerrunning = 0;
  changedate = new Date;
  response.writeHead(200, {"Content-Type": "text/plain"});
  response.end("show time");

});  





app.listen(app.get('port'), function() {
  console.log('Node app is running on port', app.get('port'));
});


