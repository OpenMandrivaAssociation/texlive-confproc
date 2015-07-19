# revision 29349
# category Package
# catalog-ctan /macros/latex/contrib/conferences/confproc
# catalog-date 2012-06-27 14:08:30 +0200
# catalog-license lppl
# catalog-version 0.8
Name:		texlive-confproc
Version:	0.8
Release:	11
Summary:	A set of tools for generating conference proceedings
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/conferences/confproc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/confproc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/confproc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/confproc.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The confproc collection comprises a class, a BibTeX style, and
some scripts for generating conference proceedings. It derives
from LaTeX scripts written for the DAFx-06 conference
proceedings, largely based on the pdfpages package for
including the proceedings papers and the hyperref package for
creating a proper table of contents, bookmarks and general
bibliography back-references. Confproc also uses many other
packages for fine tuning of the table of contents, bibliography
and index of authors. The added value of the class resides in
its time-saving aspects when designing conference proceedings.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/confproc/newapave.bst
%{_texmfdistdir}/makeindex/confproc/confproc1.ist
%{_texmfdistdir}/makeindex/confproc/confproc2.ist
%{_texmfdistdir}/tex/latex/confproc/confproc.cfg
%{_texmfdistdir}/tex/latex/confproc/confproc.cls
%{_texmfdistdir}/tex/latex/confproc/newapave.sty
%doc %{_texmfdistdir}/doc/latex/confproc/README
%doc %{_texmfdistdir}/doc/latex/confproc/buildcls.sh
%doc %{_texmfdistdir}/doc/latex/confproc/buildcppdfpapers.sh
%doc %{_texmfdistdir}/doc/latex/confproc/buildpapers.sh
%doc %{_texmfdistdir}/doc/latex/confproc/buildproc.sh
%doc %{_texmfdistdir}/doc/latex/confproc/buildprocelpb.sh
%doc %{_texmfdistdir}/doc/latex/confproc/cleancls.sh
%doc %{_texmfdistdir}/doc/latex/confproc/confproc-short.tex
%doc %{_texmfdistdir}/doc/latex/confproc/confproc.pdf
%doc %{_texmfdistdir}/doc/latex/confproc/confproc_diag.pdf
%doc %{_texmfdistdir}/doc/latex/confproc/countnbpages.sh
%doc %{_texmfdistdir}/doc/latex/confproc/example/IEEEtran.bst
%doc %{_texmfdistdir}/doc/latex/confproc/example/buildcppdfpapers.sh
%doc %{_texmfdistdir}/doc/latex/confproc/example/buildpapers.sh
%doc %{_texmfdistdir}/doc/latex/confproc/example/buildproc.sh
%doc %{_texmfdistdir}/doc/latex/confproc/example/buildprocelpb.sh
%doc %{_texmfdistdir}/doc/latex/confproc/example/countnbpages.sh
%doc %{_texmfdistdir}/doc/latex/confproc/example/dafx_06.sty
%doc %{_texmfdistdir}/doc/latex/confproc/example/example1empty.tex
%doc %{_texmfdistdir}/doc/latex/confproc/example/example2custom.tex
%doc %{_texmfdistdir}/doc/latex/confproc/example/example3optim.tex
%doc %{_texmfdistdir}/doc/latex/confproc/example/example4optim.tex
%doc %{_texmfdistdir}/doc/latex/confproc/example/exbiblio.bib
%doc %{_texmfdistdir}/doc/latex/confproc/example/exclasslastel.tex
%doc %{_texmfdistdir}/doc/latex/confproc/example/exclasslastpb.tex
%doc %{_texmfdistdir}/doc/latex/confproc/example/exclasspre.tex
%doc %{_texmfdistdir}/doc/latex/confproc/example/expages.tex
%doc %{_texmfdistdir}/doc/latex/confproc/example/expapersswitch.tex
%doc %{_texmfdistdir}/doc/latex/confproc/example/exportIndividualPDFs.sh
%doc %{_texmfdistdir}/doc/latex/confproc/example/exprogram.csv
%doc %{_texmfdistdir}/doc/latex/confproc/example/generateswitch.pl
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/IEEEtran.bst
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/dafx_06.sty
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/expages.tex
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/p_001.pdf
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/p_003.pdf
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/p_005.pdf
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/p_007.pdf
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/p_009.pdf
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/sources_pdftex/p_001/dafx_06.sty
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/sources_pdftex/p_001/fft_plot2.png
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/sources_pdftex/p_001/p_001.bib
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/sources_pdftex/p_001/p_001.tex
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/sources_pdftex/p_003/dafx_06.sty
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/sources_pdftex/p_003/fft_plot2.png
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/sources_pdftex/p_003/p_003.bib
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/sources_pdftex/p_003/p_003.tex
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/sources_pdftex/p_005/dafx_06.sty
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/sources_pdftex/p_005/fft_plot2.png
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/sources_pdftex/p_005/p_005.bib
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/sources_pdftex/p_005/p_005.tex
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/sources_pdftex/p_007/dafx_06.sty
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/sources_pdftex/p_007/fft_plot2.png
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/sources_pdftex/p_007/p_007.bib
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/sources_pdftex/p_007/p_007.tex
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/sources_tex/p_009/dafx_06.sty
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/sources_tex/p_009/fft_plot2.png
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/sources_tex/p_009/p_009.bib
%doc %{_texmfdistdir}/doc/latex/confproc/example/papers/sources_tex/p_009/p_009.tex
%doc %{_texmfdistdir}/doc/latex/confproc/example/papersinfo.sh
%doc %{_texmfdistdir}/doc/latex/confproc/example/paperssplitpreamble.sh
%doc %{_texmfdistdir}/doc/latex/confproc/example/pictures/ex_1stpage.pdf
%doc %{_texmfdistdir}/doc/latex/confproc/example/removeLaTeXcmds.sh
%doc %{_texmfdistdir}/doc/latex/confproc/example/sources_pdftex/p_001/dafx_06.sty
%doc %{_texmfdistdir}/doc/latex/confproc/example/sources_pdftex/p_001/fft_plot2.png
%doc %{_texmfdistdir}/doc/latex/confproc/example/sources_pdftex/p_001/p_001.bib
%doc %{_texmfdistdir}/doc/latex/confproc/example/sources_pdftex/p_001/p_001.tex
%doc %{_texmfdistdir}/doc/latex/confproc/example/sources_pdftex/p_003/dafx_06.sty
%doc %{_texmfdistdir}/doc/latex/confproc/example/sources_pdftex/p_003/fft_plot2.png
%doc %{_texmfdistdir}/doc/latex/confproc/example/sources_pdftex/p_003/p_003.bib
%doc %{_texmfdistdir}/doc/latex/confproc/example/sources_pdftex/p_003/p_003.tex
%doc %{_texmfdistdir}/doc/latex/confproc/example/sources_pdftex/p_005/dafx_06.sty
%doc %{_texmfdistdir}/doc/latex/confproc/example/sources_pdftex/p_005/fft_plot2.png
%doc %{_texmfdistdir}/doc/latex/confproc/example/sources_pdftex/p_005/p_005.bib
%doc %{_texmfdistdir}/doc/latex/confproc/example/sources_pdftex/p_005/p_005.tex
%doc %{_texmfdistdir}/doc/latex/confproc/example/sources_pdftex/p_007/dafx_06.sty
%doc %{_texmfdistdir}/doc/latex/confproc/example/sources_pdftex/p_007/fft_plot2.png
%doc %{_texmfdistdir}/doc/latex/confproc/example/sources_pdftex/p_007/p_007.bib
%doc %{_texmfdistdir}/doc/latex/confproc/example/sources_pdftex/p_007/p_007.tex
%doc %{_texmfdistdir}/doc/latex/confproc/example/sources_tex/p_009/dafx_06.sty
%doc %{_texmfdistdir}/doc/latex/confproc/example/sources_tex/p_009/fft_plot2.png
%doc %{_texmfdistdir}/doc/latex/confproc/example/sources_tex/p_009/p_009.bib
%doc %{_texmfdistdir}/doc/latex/confproc/example/sources_tex/p_009/p_009.tex
%doc %{_texmfdistdir}/doc/latex/confproc/example1empty.tex
%doc %{_texmfdistdir}/doc/latex/confproc/example2custom.tex
%doc %{_texmfdistdir}/doc/latex/confproc/example3optim.tex
%doc %{_texmfdistdir}/doc/latex/confproc/exbiblio.bib
%doc %{_texmfdistdir}/doc/latex/confproc/exclasslastel.tex
%doc %{_texmfdistdir}/doc/latex/confproc/exclasslastpb.tex
%doc %{_texmfdistdir}/doc/latex/confproc/exclasspre.tex
%doc %{_texmfdistdir}/doc/latex/confproc/expages.tex
%doc %{_texmfdistdir}/doc/latex/confproc/expapersswitch.tex
%doc %{_texmfdistdir}/doc/latex/confproc/exportIndividualPDFs.sh
%doc %{_texmfdistdir}/doc/latex/confproc/exprogram.csv
%doc %{_texmfdistdir}/doc/latex/confproc/generateswitch.pl
%doc %{_texmfdistdir}/doc/latex/confproc/papersinfo.sh
%doc %{_texmfdistdir}/doc/latex/confproc/paperssplitpreamble.sh
%doc %{_texmfdistdir}/doc/latex/confproc/prepareexample.sh
%doc %{_texmfdistdir}/doc/latex/confproc/removeLaTeXcmds.sh
#- source
%doc %{_texmfdistdir}/source/latex/confproc/confproc.drv
%doc %{_texmfdistdir}/source/latex/confproc/confproc.dtx
%doc %{_texmfdistdir}/source/latex/confproc/confproc.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex makeindex tex doc source %{buildroot}%{_texmfdistdir}
