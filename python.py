from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''

<html>
<head>
  <title>Semester Timetable</title>
</head>
<body>

<!-- College Logo -->
<div align="center">
  <img src="logo.png" alt="Saveetha Engineering College" width="600">
</div>

<h3 align="center">SLOT TIME TABLE - RAGA SUSANTH (212224230217)</h3>

<!-- Timetable -->
<table border="1" align="center">
  <tr><th>Day/Time</th><th>Mon</th><th>Tue</th><th>Wed</th><th>Thu</th><th>Fri</th></tr>
  <tr><td>8AM - 10AM</td><td>STATICSTICS</td><td>FREE SLOT</td><td>FREE SLOT</td><td>FREE SLOT</td><td>ADVANCED C</td></tr>
  <tr><td>10AM - 12PM</td><td>OS</td><td>ADVANCED C</td><td>WEB APPLICATION</td><td>CN</td><td>FREE SLOT</td></tr>
  <tr><td>12-1</td><td colspan="5" align="center">LUNCH</td></tr>
  <tr><td>1-3</td><td>WEB APPLICATION</td><td>HAND IN HAND</td><td>MENTOR MEET</td><td>FREE SLOT</td><td>HAND IN HAND</td></tr>
  <tr><td>3-5</td><td>CN</td><td>OS</td><td>FREE SLOT</td><td>FREE SLOT</td><td>STATICSTICS</td></tr>
</table>
`
<br>

<!-- Subject Codes -->
<table border="1" align="center">
  <tr><th>S.No</th><th>Code</th><th>Subject</th></tr>
  <tr><td>1</td><td>19AI414</td><td>Fundamentals of Web Application Development (FWAD)</td></tr>
  <tr><td>2</td><td>19MA211</td><td>Statistics and Numerical Methods(STATICSTICS)</td></tr>
  <tr><td>3</td><td>19CS405</td><td>Operating System(OS)</td></tr>
  <tr><td>4</td><td>19CS406</td><td>Computer Networks(CN)</td></tr>
  <tr><td>5</td><td>19AI305</td><td>Advanced C Programming</td></tr>
  <tr><td>6</td><td>19CS570</td><td>Entrepreneurship and Small Business Development(HAND IN HAND)</td></tr>
</table>

</body>
</html>
'''
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()