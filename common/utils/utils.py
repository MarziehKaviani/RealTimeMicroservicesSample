from rest_framework.response import Response

from common.statics import *


class BaseResponse(Response):
    def __init__(self,  http_status_code, is_exception, message='Unknown', business_status_code=-1, data=None) -> None:
        super().__init__(
            data={
                DATA: data,
                MESSAGE: message,
                BUISSINES_STATUS_CODE: business_status_code
            },
            status=http_status_code,
            exception=is_exception
        )