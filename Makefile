.PHONY: all test release devenv publish

all: devenv release

test: release
#	Run tests
	./node_modules/.bin/syntaxdev test --tests test/**/*.py --syntax grammars/src/MagicSetonas.syntax.yaml
	./node_modules/.bin/syntaxdev test --tests test/**/*.re --syntax grammars/src/MagicRegExp.syntax.yaml

# 	Check if the version specified in "package.json" matches the latest git tag
	@if [ \
		`cat package.json | grep -e '^[[:space:]]*"version":' | sed -e 's/[[:space:]]*"version":[[:space:]]*"\(.*\)",/\1/'` \
		!= \
		`git describe --tags --abbrev=0 | sed -e 's/v\([[:digit:]]\{1,\}\.[[:digit:]]\{1,\}\.[[:digit:]]\{1,\}\).*/\1/'` \
	] ; \
		then echo "Error: package.version != git.tag" && exit 1 ; fi

devenv:
	npm install syntaxdev@0.0.13

release:
	./node_modules/.bin/syntaxdev build-plist --in grammars/src/MagicSetonas.syntax.yaml --out grammars/MagicSetonas.tmLanguage
	./node_modules/.bin/syntaxdev build-plist --in grammars/src/MagicRegExp.syntax.yaml --out grammars/MagicRegExp.tmLanguage

	./node_modules/.bin/syntaxdev build-cson --in grammars/src/MagicSetonas.syntax.yaml --out grammars/MagicSetonas.cson
	./node_modules/.bin/syntaxdev build-cson --in grammars/src/MagicRegExp.syntax.yaml --out grammars/MagicRegExp.cson

	./node_modules/.bin/syntaxdev scopes --syntax grammars/src/MagicSetonas.syntax.yaml > misc/scopes

publish: test
	apm publish major
	rm -rf ./node_modules/syntaxdev
	vsce publish
