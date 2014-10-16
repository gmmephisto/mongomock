MAIN_TREE := HEAD
MAIN_COMMIT := $(shell git rev-parse --verify $(MAIN_TREE))
PKG_NAME := python-mongomock
PROG_NAME := $(shell sed -n s/%define[[:space:]]*pkgname[[:space:]]*//p $(PKG_NAME).spec)
VERSION := $(shell sed -n s/[[:space:]]*Version:[[:space:]]*//p $(PKG_NAME).spec)

sources:
	@git archive --format=tar --prefix="$(PROG_NAME)-$(VERSION)/" \
		$(MAIN_COMMIT) | gzip > "$(PROG_NAME)-$(VERSION).tar.gz"

default: test

detox-test:
	detox

travis-test: test

test: env
	.env/bin/nosetests -w tests

coverage-test: env
	.env/bin/coverage run .env/bin/nosetests -w tests

env: .env/.up-to-date

.env/.up-to-date: setup.py Makefile
	virtualenv .env
	.env/bin/pip install -e .
	.env/bin/pip install nose coverage PyExecJS pymongo
	touch .env/.up-to-date

.PHONY: doc

