class CustomExceptionFloatError(Exception):

    def __str__(self):
        return "Provided value must be integer. Float eas given"


class CustomExceptionStringError(Exception):

    def __str__(self):
        return "Provided value must be integer. String was given"
