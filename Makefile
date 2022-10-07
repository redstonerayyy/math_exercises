.PHONY: build
build:
	mkdir -p ./build
	python latexbuild/latexbuild.py

clean:
	rm -rf ./build
	find ./material ! -name '.gitkeep' -type f -exec rm -f {} +
	find ./material/* ! -name '.gitkeep' -type d -exec rm -rf {} +
