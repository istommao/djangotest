import time
import json
from django.utils.deprecation import MiddlewareMixin
import urllib.parse
import logging

logger = logging.getLogger(__name__)


class LogDeleteRequestMiddle(MiddlewareMixin):

    def process_request(self, request):
        request.init_time = time.time()

        return None

    def process_response(self, request, response):
        if request.method != 'DELETE':
            return response

        try:
            localtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            path = request.path
            method = request.method
            status_code = response.status_code
            content = response.content
            content = str(content.decode('utf-8'))
            content = urllib.parse.unquote(content)
            content = (json.loads(content))
            message = '%s %s %s %s %s' % (localtime, path, method, status_code, content)
            logger.info(message)
        except Exception as err:
            # 记录log 收集到 sentry等告警平台
            logger.critical('系统错误')

        return response
