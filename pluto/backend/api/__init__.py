# coding:utf8

"""
Copyright 2016 Smallpay Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from flask import request
from flask_restful import Resource, reqparse, abort
from werkzeug.exceptions import HTTPException

from pluto.util.log import logger
from pluto.backend import db


class ApiResource(Resource):

    _query_arguments = []

    def __init__(self):
        self.arg_namespace = None
        self.session = db.session

    def get_argument(self, name):
        return self.arg_namespace.get(name) if self.arg_namespace else None

    def parse_body_to_model(self, model_class):
        req_body = request.get_json(force=True)
        model = model_class()
        model.from_dict(req_body)
        return model

    def dispatch_request(self, *args, **kwargs):
        if self._query_arguments and request.method == 'GET':
            arg_parser = reqparse.RequestParser()
            arg_parser.args = self._query_arguments
            self.arg_namespace = arg_parser.parse_args()
        try:
            resp = super(ApiResource, self).dispatch_request(*args, **kwargs)
            return resp
        except HTTPException:
            raise
        except Exception as e:
            logger.exception("系统异常")
            abort(500, message=e.message)
