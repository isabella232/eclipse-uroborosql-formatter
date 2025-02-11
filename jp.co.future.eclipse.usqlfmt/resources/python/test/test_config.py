# coding:utf-8
'''
Created on 2016/07/27

@author: ota
'''

import unittest
from uroborosqlfmt.config import LocalConfig
import uroborosqlfmt


class Test(unittest.TestCase):

    def test_uppercase_config(self):
        self.assertEqual(format_sql("""
        select * from DUAL
        """, LocalConfig().set_case('lower')),
"""select
\t*
from
\tdual"""
        )


        self.assertEqual(format_sql("""
        select * from DUAL
        """, LocalConfig().set_case('upper')),
"""SELECT
\t*
FROM
\tDUAL"""
        )

        self.assertEqual(format_sql("""
        select * from DUAL
        """, LocalConfig().set_case('capitalize')),
"""Select
\t*
From
\tDual"""
        )

def format_sql(text, config):
    return uroborosqlfmt.format_sql(text, config)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
