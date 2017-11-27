from flask.views import MethodView

from task_tracker_api.decorators import jsonified, jwt_auth
from task_tracker_api.main import app


class ProjectAPI(MethodView):
    @jwt_auth
    @jsonified
    def post(self, json):
        """C in CRUD"""
        return {'data': json, 'method': 'create project'}

    @jwt_auth
    @jsonified
    def get_all(self):
        """R in CRUD"""
        return {'data': {}, 'method': 'read all projects'}

    @jwt_auth
    @jsonified
    def get_one(self, id):
        """R in CRUD"""
        return {'data': {}, 'method': 'read project {}'.format(str(id))}

    def get(self, id):
        return self.get_all() if id is None else self.get_one(id)

    @jwt_auth
    @jsonified
    def put(self, json, id):
        """U in CRUD"""
        return {'data': json, 'method': 'update project {}'.format(str(id))}

    @jwt_auth
    @jsonified
    def delete(self, json, id):
        """D in CRUD"""
        return {'data': json, 'method': 'delete project {}'.format(str(id))}


project_view = ProjectAPI.as_view('project_api')
app.add_url_rule('/v1/project', view_func=project_view, methods=['POST'])
app.add_url_rule('/v1/project', defaults={'id': None},
                 view_func=project_view, methods=['GET'])
app.add_url_rule('/v1/project/<int:id>', view_func=project_view,
                 methods=['GET', 'PUT', 'DELETE'])
