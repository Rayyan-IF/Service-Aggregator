def ResponseException(message):
    response_messages = {
        200: "Request fulfilled, Here's the response",
        201: "Request created",
        202: "Request accepted",
        204: "Request fulfilled, Nothing to response",
        400: "Bad request or invalid syntax",
        401: "No permission, check authorization",
        403: "Request forbidden, cannot access",
        404: "Nothing matching request",
        405: "Request methods invalid",
        406: "Request not accepted",
        408: "Request timeout, try again later",
        409: "Request conflict",
        418: "Server refuses to brew coffee because it is a teapot"
    }
    return response_messages.get(message, message)