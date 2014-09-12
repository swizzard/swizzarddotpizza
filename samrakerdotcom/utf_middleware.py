import re

class MySQLUnicodeFixingMiddleware(object):

    INVALID_UTF8_RE = re.compile(u'[^\u0000-\uD7FF\uE000-\uFFFF]', re.UNICODE)

    def process_request(self, request):
        """Replace 4-byte unicode characters by REPLACEMENT CHARACTER"""
        request.POST = request.POST.copy()
        request.GET = request.GET.copy()
        request = request.POST or request.GET
        for key, values in request.iterlists():
            request.setlist(key,
                [self.INVALID_UTF8_RE.sub(u'\uFFFD', v) for v in values])
