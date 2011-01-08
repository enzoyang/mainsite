import web
from views.hello2 import hello2
urls = ('/',hello2)

app = web.application(urls,globals())

class hello:
    def GET(self):
        return 'hello world'

if __name__ == '__main__':
    app.run();