from flask import jsonify
from flask.views import MethodView
from QueryController.query5 import Query5

class Query5API(MethodView):
    def __init__(self):
        self.q5=Query5()

    def get(self):
        result5= self.q5.execute5()
        return jsonify(result5)