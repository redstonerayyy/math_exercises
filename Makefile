build:
	mkdir -p ./build
	pdflatex -output-directory ./build ./src/latex_template.tex ./src/latex_template copy.tex
	cp