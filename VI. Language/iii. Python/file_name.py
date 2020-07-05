import inspec
print inspect.getfile( inspect.currentframe() )

import os
print os.path.abspath( __file__ )
 
import sys
sys._getframe().f_code.co_filename 

# Reference: https://oktopbang.tistory.com/entry/%ED%98%84%EC%9E%AC-%EC%9E%91%EC%97%85%ED%95%98%EA%B3%A0-%EC%9E%88%EB%8A%94-%EC%86%8C%EC%8A%A4%EC%9D%98-%ED%8C%8C%EC%9D%BC-%EC%9D%B4%EB%A6%84-%EC%95%8C%EC%95%84%EC%98%A4%EB%8A%94-%EB%B0%A9%EB%B2%95
