Feature: It is alive

    Scenario: Health Check
        Given a endpoint of '/health'
        When a GET request is made to the endpoint
        Then the endpoint should respond with http status code OK
        and the endpoint should return a link to the service documentation

