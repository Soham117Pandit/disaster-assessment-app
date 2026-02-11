def success_response(message, data=None):
    response = {"message": message}
    if data:
        response["data"] = data
    return response
