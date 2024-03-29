class HttpError(Exception):
    pass


class InternalServerError(HttpError):
    status_code = 500

    def __int__(self, msg="Internal Server Error"):
        super().__init__(msg, {})
        self.message = msg
        self.error_dict = {}


class BadRequestError(HttpError):
    status_code = 400

    def __int__(self, msg="Bad Request"):
        super().__init__(msg, {})
        self.message = msg
        self.error_dict = {}


class UnAuthorizedError(HttpError):
    status_code = 401

    def __int__(self, msg="Invalid Credentials"):
        super().__init__(msg, {})
        self.message = msg
        self.error_dict = {}


class ForbiddenError(HttpError):
    status_code = 403

    def __int__(self, msg="Forbidden Error"):
        super().__init__(msg, {})
        self.message = msg
        self.error_dict = {}


class NotFoundError(HttpError):
    status_code = 403

    def __int__(self, msg="Not Found Error"):
        super().__init__(msg, {})
        self.message = msg
        self.error_dict = {}


class RateLimitError(HttpError):
    status_code = 429

    def __int__(self, msg="About To Hit Rate Limit"):
        super().__init__(msg, {})
        self.message = msg
        self.error_dict = {}


class SQLAlchemyIntegrityError(HttpError):
    status_code = 429

    def __int__(self, msg="A Database Error Occurred Due To A Bad Request"):
        super().__init__(msg, {})
        self.message = msg
        self.error_dict = {}
