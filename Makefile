include .env

.PHONY: init
init:
	./init.sh

.PHONY: login
login:
	poetry shell
	oj login -u ${UNAME} -p ${PASSWD} "https://atcoder.jp/"
