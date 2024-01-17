
all:
	# pdflatex main.tex pdf -o main.pdf
	pdflatex presentation.tex pdf -o pres.pdf
	rm -rf  *.aux *.log *.fls *.fdb_latexmk *.fls *.gz *.fdb_latexmk

.PHONY : clean
clean:
	rm -rf $(PREF_OBJ)*.o $(TARGET) *.aux *.log vgcore.* *.vrb *.snm *.nav *.out *.fls *.toc *.gz
