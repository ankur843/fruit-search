var el = x => document.getElementById(x);



function analyze() {

  el("analyze-button").innerHTML = "Searching...";
  var xhr = new XMLHttpRequest();
  var loc = window.location;
   
	urlstr="http://"+loc.hostname+":"+loc.port+"/analyze";
	
   
    xhr.open( "GET", urlstr, false ); // false for synchronous request
    xhr.send( null );
	el("result-label").innerHTML = xhr.responseText;
   el("analyze-button").innerHTML = "Search";
  //el("result-label").innerHTML = urlstr+"zell";
  
  
  xhr.onerror = function() {
	  el("analyze-button").innerHTML = "done";
    alert(xhr.responseText);
  };
  xhr.onload = function(e) {
    if (this.readyState === 4) {
		el("analyze-button").innerHTML = "done";
      var response = JSON.parse(e.target.responseText);
	  el("result-label").innerHTML = 'Got it! Youre sea';
      //el("result-label").innerHTML = `Got it! You're searching for ${response["result"]}`;
    }
    el("analyze-button").innerHTML = "Search";
  };


}