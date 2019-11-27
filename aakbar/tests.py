# -*- coding: utf-8 -*-
'''Implements shell-level testing'''
from pytest_shutil import workspace, path

# Enable the fixture explicitly in your tests or conftest.py (not required when using setuptools entry points)
pytest_plugins = ['pytest_shutil']

def test_something(workspace):
    # Workspaces contain a handle to the path.py path object (see https://pathpy.readthedocs.io/)
    path = workspace.workspace
    script = path / 'hello.sh'
    script.write_text('#!/bin/sh\n echo hello world!')
    print('hello from test_something!')
    # There is a 'run' method to execute things relative to the workspace root
    workspace.run('hello.sh')