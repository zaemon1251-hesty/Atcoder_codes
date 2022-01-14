chcp 65001

rem activate virtual environment
call %4


set problem_name=%~n1
set test_dir=AtCoder\onlinejudge\test\%problem_name%\
set base_url=%~n3
set code_path=%2

rem make test directory
if not exist "%test_dir%" (
    oj dl -d %test_dir% https://atcoder.jp/contests/%base_url%/tasks/%problem_name:-=_%
)

rem run test
oj test -c "python %code_path%" -d "%test_dir%"
