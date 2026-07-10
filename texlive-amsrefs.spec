%global tl_name amsrefs
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.14
Release:	%{tl_revision}.1
Summary:	A LaTeX-based replacement for BibTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/amsrefs
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amsrefs.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amsrefs.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/amsrefs.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Amsrefs is a LaTeX package for bibliographies that provides an archival
data format similar to the format of BibTeX database files, but adapted
to make direct processing by LaTeX easier. The package can be used
either in conjunction with BibTeX or as a replacement for BibTeX.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/bibtex/bib
%dir %{_datadir}/texmf-dist/bibtex/bst
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/bibtex/bib/amsrefs
%dir %{_datadir}/texmf-dist/bibtex/bst/amsrefs
%dir %{_datadir}/texmf-dist/doc/latex/amsrefs
%dir %{_datadir}/texmf-dist/source/latex/amsrefs
%dir %{_datadir}/texmf-dist/tex/latex/amsrefs
%{_datadir}/texmf-dist/bibtex/bib/amsrefs/amsj.bib
%{_datadir}/texmf-dist/bibtex/bst/amsrefs/amsra.bst
%{_datadir}/texmf-dist/bibtex/bst/amsrefs/amsrn.bst
%{_datadir}/texmf-dist/bibtex/bst/amsrefs/amsrs.bst
%{_datadir}/texmf-dist/bibtex/bst/amsrefs/amsru.bst
%{_datadir}/texmf-dist/bibtex/bst/amsrefs/amsry.bst
%doc %{_datadir}/texmf-dist/doc/latex/amsrefs/amsrdoc.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amsrefs/amsrefs.faq
%doc %{_datadir}/texmf-dist/doc/latex/amsrefs/amsrefs.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amsrefs/amsxport.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amsrefs/changes.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amsrefs/cite-xa.tex
%doc %{_datadir}/texmf-dist/doc/latex/amsrefs/cite-xb.tex
%doc %{_datadir}/texmf-dist/doc/latex/amsrefs/cite-xh.tex
%doc %{_datadir}/texmf-dist/doc/latex/amsrefs/cite-xs.tex
%doc %{_datadir}/texmf-dist/doc/latex/amsrefs/gktest.ltb
%doc %{_datadir}/texmf-dist/doc/latex/amsrefs/ifoption.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amsrefs/jr.bib
%doc %{_datadir}/texmf-dist/doc/latex/amsrefs/mathscinet.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amsrefs/pcatcode.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amsrefs/rkeyval.pdf
%doc %{_datadir}/texmf-dist/doc/latex/amsrefs/textcmds.pdf
%doc %{_datadir}/texmf-dist/source/latex/amsrefs/README
%doc %{_datadir}/texmf-dist/source/latex/amsrefs/amsrdoc.tex
%doc %{_datadir}/texmf-dist/source/latex/amsrefs/amsrefs.dtx
%doc %{_datadir}/texmf-dist/source/latex/amsrefs/amsrefs.ins
%doc %{_datadir}/texmf-dist/source/latex/amsrefs/amsxport.dtx
%doc %{_datadir}/texmf-dist/source/latex/amsrefs/amsxport.ins
%doc %{_datadir}/texmf-dist/source/latex/amsrefs/changes.tex
%doc %{_datadir}/texmf-dist/source/latex/amsrefs/ifoption.dtx
%doc %{_datadir}/texmf-dist/source/latex/amsrefs/ifoption.ins
%doc %{_datadir}/texmf-dist/source/latex/amsrefs/install.txt
%doc %{_datadir}/texmf-dist/source/latex/amsrefs/manifest.txt
%doc %{_datadir}/texmf-dist/source/latex/amsrefs/mathscinet.dtx
%doc %{_datadir}/texmf-dist/source/latex/amsrefs/mathscinet.ins
%doc %{_datadir}/texmf-dist/source/latex/amsrefs/pcatcode.dtx
%doc %{_datadir}/texmf-dist/source/latex/amsrefs/pcatcode.ins
%doc %{_datadir}/texmf-dist/source/latex/amsrefs/rkeyval.dtx
%doc %{_datadir}/texmf-dist/source/latex/amsrefs/rkeyval.ins
%doc %{_datadir}/texmf-dist/source/latex/amsrefs/textcmds.dtx
%doc %{_datadir}/texmf-dist/source/latex/amsrefs/textcmds.ins
%{_datadir}/texmf-dist/tex/latex/amsrefs/amsbst.sty
%{_datadir}/texmf-dist/tex/latex/amsrefs/amsrefs.sty
%{_datadir}/texmf-dist/tex/latex/amsrefs/ifoption.sty
%{_datadir}/texmf-dist/tex/latex/amsrefs/mathscinet.sty
%{_datadir}/texmf-dist/tex/latex/amsrefs/pcatcode.sty
%{_datadir}/texmf-dist/tex/latex/amsrefs/rkeyval.sty
%{_datadir}/texmf-dist/tex/latex/amsrefs/textcmds.sty
