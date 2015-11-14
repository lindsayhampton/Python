import webapp2

class MainHandler(webapp2.RequestHandler):
    def get(self):

        p = Page()
        p.body = '''
        <p>I love Python</p>
        <h1>I also love Vodka</h1>
        '''

        p.title = "I LOVE BEER"
        html = p.print_out()
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)

class Page(object):
        def __init__(self):
            self.title = ""
            self.head = '''
            <!DOCTYPE>
            <html>
                <head>
                    <title>{self.title}</title>
                </head>
                <body>
            '''
            self.body = ""
            self.close = '''
            </body>
            </html>
                        '''

        def print_out(self):
            all = (self.head + self.body + self.close).format(**locals())
            return all