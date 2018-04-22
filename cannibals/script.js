// Set up!
var a_canvas = document.getElementById("a");
var context = a_canvas.getContext("2d");
var HEIGHT = 25;
var WIDTH = 25;
var fH = 500;
var fW = 500;
var cH = fH/HEIGHT;
var cW = fW/WIDTH;

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
};

function mod(n, m) {
        return ((n % m) + m) % m;
};

function httpGetAsync(theUrl, callback)
{
    var xmlHttp = new XMLHttpRequest();
    xmlHttp.onreadystatechange = function() { 
        if (xmlHttp.readyState == 4 && xmlHttp.status == 200)
            callback(xmlHttp.responseText);
    }
    xmlHttp.open("GET", theUrl, true); // true for asynchronous 
    xmlHttp.send(null);
}

function update(stuff) {
    context.fillRect(50, 50, 50, 50)
}

var id = setInterval(frame, 10);

function frame() {
    httpGetAsync("https://iothackhotspots.herokuapp.com/read", update())
}
