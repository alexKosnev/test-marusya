import aiohttp
from aiohttp import web
import os

TOKEN = "7e03be3a7a811b10d93a62d43e119d09fd6e1d4fdb30b7f9de98da001270"
HOST_PORT = int(os.environ.get('PORT', '8443'))
updater = Updater(TOKEN)
# add handlers
updater.start_webhook(listen="0.0.0.0",
                      port=PORT,
                      url_path=TOKEN,
                      webhook_url="https://test-marusya.herokuapp.com/" + TOKEN)
updater.idle()


HOST_IP = "0.0.0.0"

async def skill_space(request_obj):
    request = await request_obj.json()
    
    response = {}
    response["version"] = request["version"]
    response["session"] = request["session"]
    response["response"] = { "end_session" : False }
    
    response["response"]["text"] = "Привет!"
    response["response"]["end_session"] = True
    
    return web.json_response(response)
    
    
def init():
    app = web.Application()
    app.router.add_post("/skill_space", skill_space)
    web.run_app(app, host = HOST_IP, port = HOST_PORT)
    
if __name__ == "__main__":
    init()