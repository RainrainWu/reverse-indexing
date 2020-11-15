def build_status(code, message):
    return {
        "status": code,
        "message": message
    }


def build_hateoas(links, status, data, embedded):
    return {
        "_links": links,
        "status": status,
        "data": data,
        "_embedded": embedded
    }