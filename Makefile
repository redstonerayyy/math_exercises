.PHONY: build

build:
	./src/latexbuild.sh

clean:
	rm -rf ./build
	find ./material/* ! -name '.gitkeep' -type f -exec rm -f {} + ; 2>/dev/null
	find ./material/* ! -name '.gitkeep' -type d -exec rm -rf {} + ; 2>/dev/null
	find ./src/** ! -name '*.tex' ! -name '*.py' ! -name '*.txt' ! -name '*.sh' -type f -exec rm -rf {} + ; 2>/dev/null
