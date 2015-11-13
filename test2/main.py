import webapp2

# Make classes for HTML and add them to mainhandler


class MainHandler(webapp2.RequestHandler):
    def get(self):
        #self.response.write('<h1>Hello world!</h1>')
        p = Page()
        print self.request.GET
        if self.request.GET:
            print "<p>Form Data Exists!</p>"
        else:
            p.body = '''
        <form method="GET">
            <label>What is your name?:</label>
            <input type="text" name="username" placeholder="i.e. John Doe">
            <button type="submit">Let's Go!</button>
        </form>
'''

        self.response.write(p.print_out())

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

class Page(object):
    def __init__(self):
        self.head = '''
<!doctype HTML>
<html>
    <head>
        <title>Beer</title>
        <link rel="stylesheet" href="css/styles.css" type="text/css">
    </head>
    <body>
'''
        self.body = ""
        self.close = '''
    </body>
</html>
'''
    def print_out(self):
        all = self.head + self.body + self.close
        return all