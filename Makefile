all: build/main.pdf

# hier Python-Skripte:
build/plot1.pdf: content/Python/plot1.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python content/Python/plot1.py

build/plot2.pdf: content/Python/plot2.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python content/Python/plot2.py

build/plot3.pdf: content/Python/plot3.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python content/Python/plot3.py

build/plot4.pdf: content/Python/plot4.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python content/Python/plot4.py

build/diff1.pdf: content/Python/diff1.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python content/Python/diff1.py

build/diff2.pdf: content/Python/diff2.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python content/Python/diff2.py

build/plot5.pdf: content/Python/plot5.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS=$$(pwd): python content/Python/plot5.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/plot1.pdf build/plot2.pdf build/plot3.pdf build/plot4.pdf build/diff1.pdf build/diff2.pdf build/plot5.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS=build: \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
