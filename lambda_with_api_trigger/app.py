import sys
sys.path.insert(0, './pymadeeasy')
from chalice import Chalice, BadRequestError, NotFoundError
from operating_system_functions import get_current_date_time_url_str

app = Chalice(app_name="lambda_with_api_trigger_%s" % (get_current_date_time_url_str()))
app.debug = True

# https://www.w3schools.com/tags/ref_httpmethods.asp
HTTP_METHODS = ['GET', 'POST', 'PUT', 'HEAD', 'DELETE', 'PATCH', 'OPTIONS']

OBJECTS = {
}


# root removed in case the API is left open
# @app.route('/', methods=['GET'])
# def index():
#     return {'hello': 'world'}


@app.route('/hello/{name}', methods=['GET'])
def say_hello(name):
    return {'hello': (name, 'nice to meet you')}


# ADDITIONAL EXAMPLES
# @app.route('/cities/{city}', methods=HTTP_METHODS)
# def state_of_city(city):
#     try:
#         return {'state': CITIES_TO_STATE[city]}
#     except KeyError:
#         raise BadRequestError("Unknown city '%s', valid choices are: %s" % (city, ', '.join(CITIES_TO_STATE.keys())))
#
# @app.route('/myview', methods=['POST'])
# def myview_post():
#     pass
#
# @app.route('/myview', methods=['PUT'])
# def myview_put():
#     pass

# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
