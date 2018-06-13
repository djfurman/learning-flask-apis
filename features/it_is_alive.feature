Feature: It is alive
As an API consumer or system administrator
I need to know if the application is alive and listening for traffic

    @atdd @#1
    Scenario: Health Check
        Given a endpoint of '/health'
        When a GET request is made to the endpoint
        Then the endpoint should respond with http status code OK
        and the endpoint should return a link to the service documentation

