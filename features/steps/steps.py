from behave import *

@given(u'a endpoint of \'/health\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a endpoint of \'/health\'')


@when(u'a GET request is made to the endpoint')
def step_impl(context):
    raise NotImplementedError(u'STEP: When a GET request is made to the endpoint')


@then(u'the endpoint should respond with http status code OK')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the endpoint should respond with http status code OK')


@then(u'the endpoint should return a link to the service documentation')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the endpoint should return a link to the service documentation')
