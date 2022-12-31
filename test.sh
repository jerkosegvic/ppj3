for test in lab3_teza/*; do python SemantickiAnalizator.py < $test/test.in > a.out; echo $test; diff a.out $test/test.out; done;
