import unittest

import vivisect.lib.bexfile as v_bexfile

class BexFileTest(unittest.TestCase):

    def test_bexfile_info(self):

        class FakeBex(v_bexfile.BexFile):
            def _bex_info_woot(self):
                return 10

        bex = FakeBex(None)
        self.assertEqual( bex.info('woot'), 10 )

    def test_bexfile_baseaddr(self):

        class FakeBex(v_bexfile.BexFile):
            def _bex_baseaddr(self):
                return 10

        bex = FakeBex(None)
        self.assertEqual( bex.baseaddr(), 10 )

    #def test_bexfile_add(self):
