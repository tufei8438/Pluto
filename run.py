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
from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware
from pluto.backend import app as backend
from pluto.frontend import app as frontend


application = DispatcherMiddleware(frontend, {
    '/api': backend
})


if __name__ == '__main__':
    run_simple('0.0.0.0', 5000, application, use_reloader=True, use_debugger=True)
