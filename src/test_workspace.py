import os
import urlparse

import requests

from workspace import cache, local, remote, tmp


class TestWorkspace(object):
    def test_tmp(self):
        with tmp() as ofolder:
            assert os.path.exists(ofolder)
            assert os.path.isdir(ofolder)

        assert not os.path.exists(ofolder)

    def test_cache(self):
        @cache(u'./tmp/{0}-{1}-{2}')
        def _test(a, b, c, opath):
            with open(opath, 'w') as ofile:
                ofile.write('%s-%s-%s' % (a, b, c))

            return opath

        opath = _test('a', 'b', 'c')

        assert os.path.basename(opath) == 'a-b-c'
        assert os.path.exists(opath)
        assert open(opath).read() == 'a-b-c'

    def test_local(self):
        ofile = local('http://via.placeholder.com/350x150.jpg')

        assert os.path.basename(ofile) == '59dedab3-99f.jpe'

    def test_remote(self):
        url = remote('./350x150.jpg')
        resp = requests.get(url)
        assert resp.status_code == 200
