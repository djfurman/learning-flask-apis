from behave import *
import requests
from http import HTTPStatus

@given(u'a endpoint of \'/health\'')
def step_impl(context):
    context.uri = 'http://localhost:5000/health'


@when(u'a GET request is made to the endpoint')
def step_impl(context):
    context.response = requests.get(context.uri)


@then(u'the endpoint should respond with http status code OK')
def step_impl(context):
    assert context.response.status_code == HTTPStatus.OK


@then(u'the endpoint should return a link to the service documentation')
def step_impl(context):
    assert context.response.json()['docs'] is not None
