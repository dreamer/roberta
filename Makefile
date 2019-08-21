.PHONY: lint test coverage \
	check-formatting pretty-code \
	install uninstall \
	user-install user-uninstall \
	clean shortlog \
	compatibilitytool.vdf version.py

# These variables are used to generate compatibilitytool.vdf:
#
tool_name             = roberta
tool_name_dev         = roberta_dev
tool_name_display     = Roberta (native ScummVM)
tool_name_display_dev = Roberta (dev)

# Default names for installation directories:
#
tool_dir              = roberta
tool_dir_dev          = roberta-dev

files = run-vm \
	fakescripteval.py \
	log.py \
	settings.py \
	toolbox.py \
	tweaks.py \
	version.py \
	xdg.py \
	xlib.py \
	compatibilitytool.vdf \
	toolmanifest.vdf \
	LICENSE \
	README.md

ifeq ($(origin XDG_DATA_HOME), undefined)
	data_home := ${HOME}/.local/share
else
	data_home := ${XDG_DATA_HOME}
endif

# These two variables are to be overriden by packagers, for situations
# when source code is downloaded as a tarball, e.g.:
#
# make prefix=/usr version=v%{version} install
#
prefix = /usr/local
version = $(shell git describe --tags --dirty --always)

install_dir = $(DESTDIR)$(prefix)/share/steam/compatibilitytools.d/$(tool_dir)
devel_install_dir = $(data_home)/Steam/compatibilitytools.d/$(tool_dir_dev)

lint: version.py
	shellcheck scripts/codestyle.sh tests/coverage-report.sh
	pylint --rcfile=.pylint run-vm *.py tests/*.py

test:
	XDG_CONFIG_HOME=$(shell pwd)/tests/files/xdg_config_home \
	LUX_QUIET=1 python3 -m unittest discover -v -s tests

coverage:
	bash tests/coverage-report.sh 2> /dev/null

compatibilitytool.vdf: compatibilitytool.template
	sed 's/%name%/$(tool_name)/; s/%display_name%/$(tool_name_display)/' $< > $@

version.py:
	@echo "# pylint: disable=missing-docstring" > $@
	@echo "VERSION = '$(version)'" >> $@

$(tool_dir).zip: $(files)
	mkdir -p $(tool_dir)
	cp --reflink=auto -t $(tool_dir) $^
	zip $@ $(tool_dir)/*
	rm -rf $(tool_dir)
	./run-vm --version

$(tool_dir).tar.xz: $(files)
	mkdir -p $(tool_dir)
	cp --reflink=auto -t $(tool_dir) $^
	tar -cJf $@ $(tool_dir)
	rm -rf $(tool_dir)
	./run-vm --version

install: $(files)
	mkdir -p $(install_dir)
	cp --reflink=auto -t $(install_dir) $^

uninstall:
	rm -rf $(install_dir)

user-install: tool_name = $(tool_name_dev)
user-install: tool_name_display = $(tool_name_display_dev)
user-install: $(files)
	mkdir -p $(devel_install_dir)
	cp --reflink=auto -t $(devel_install_dir) $^

user-uninstall:
	rm -rf $(devel_install_dir)

clean:
	rm -f compatibilitytool.vdf
	rm -f version.py
	rm -f preconfig.tar
	rm -f $(tool_dir).tar.xz
	rm -f $(tool_dir).zip

# Summary to be included in CHANGELOG.md
shortlog:
	git shortlog $(shell git describe --tags --abbrev=0)..HEAD

check-formatting:
	yapf --version
	bash scripts/codestyle.sh --max-line-length=80 run-vm *.py
	yapf -d -vv run-vm *.py scripts/*.py

pretty-code:
	yapf -i -vv run-vm *.py
	git status
