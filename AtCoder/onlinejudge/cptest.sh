#!/bin/bash

problem_name=$1
problem_name=${problem_name##*/}
test_dir=AtCoder/onlinejudge/test/${problem_name}
base_url=${problem_name%_*}
code_path=$2

# make test directory
if [ ! -e ${test_dir} ]; then
    oj dl -d ${test_dir} https://atcoder.jp/contests/${base_url}/tasks/${problem_name//-/_}
fi

oj test -c "python $code_path" -d $test_dir
