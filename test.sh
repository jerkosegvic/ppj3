for test in 1_t/*; do python SemantickiAnalizator.py < $test/test.in > a.out; echo $test; diff a.out $test/test.out; done;
