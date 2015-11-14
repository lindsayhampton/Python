import webapp2

class Page(object):
    def __init__(self):
        self.head = '''
<!doctype HTML>
<html>
    <head>
        <title>A Simple Form by Lindsay Hampton</title>
        <link rel="stylesheet" href="css/styles.css" type="text/css">
    </head>
    <body>
'''
        self.body = '''
        <form method="GET">
            <label>What is your first name?:</label>
            <input type="text" name="firstname" placeholder="i.e. John">
            <label>What is your last name?:</label>
            <input type="text" name="lastname" placeholder="i.e. Smith">
            <label>How old are you?:</label>
            <input type="text" name="age" placeholder="i.e. 12">

            <button type="submit">Let's Go!</button>
        </form>
'''
        self.close = '''
    </body>
</html>
'''
    def print_out(self):
        all = self.head + self.body + self.close
        return all

class MainHandler(webapp2.RequestHandler):
    def get(self):
        p = Page()
        print self.request.GET
        if self.request.GET:
            firstname = self.request.GET["firstname"]
            lastname = self.request.GET["lastname"]
            age = self.request.GET["age"]

            p.body = ''' <h1>Form Data Exists!</h1> '''

        self.response.write(p.print_out())


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
