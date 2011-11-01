Name:		texlive-amsrefs
Version:	2.09
Release:	1
Summary:	A LaTeX-based replacement for BibTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/amsrefs
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsrefs.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsrefs.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/amsrefs.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Amsrefs is a LaTeX package for bibliographies that provides an
archival data format similar to the format of BibTeX database
files, but adapted to make direct processing by LaTeX easier.
The package can be used either in conjunction with BibTeX or as
a replacement for BibTeX.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    %_texmf_mktexlsr_preun

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mltexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bib/amsrefs/amsj.bib
%{_texmfdistdir}/bibtex/bst/amsrefs/amsra.bst
%{_texmfdistdir}/bibtex/bst/amsrefs/amsrn.bst
%{_texmfdistdir}/bibtex/bst/amsrefs/amsrs.bst
%{_texmfdistdir}/bibtex/bst/amsrefs/amsru.bst
%{_texmfdistdir}/bibtex/bst/amsrefs/amsry.bst
%{_texmfdistdir}/tex/latex/amsrefs/amsbst.sty
%{_texmfdistdir}/tex/latex/amsrefs/amsrefs.sty
%{_texmfdistdir}/tex/latex/amsrefs/ifoption.sty
%{_texmfdistdir}/tex/latex/amsrefs/mathscinet.sty
%{_texmfdistdir}/tex/latex/amsrefs/pcatcode.sty
%{_texmfdistdir}/tex/latex/amsrefs/rkeyval.sty
%{_texmfdistdir}/tex/latex/amsrefs/textcmds.sty
%doc %{_texmfdistdir}/doc/latex/amsrefs/amsrdoc.pdf
%doc %{_texmfdistdir}/doc/latex/amsrefs/amsrefs.faq
%doc %{_texmfdistdir}/doc/latex/amsrefs/amsrefs.pdf
%doc %{_texmfdistdir}/doc/latex/amsrefs/amsxport.pdf
%doc %{_texmfdistdir}/doc/latex/amsrefs/changes.pdf
%doc %{_texmfdistdir}/doc/latex/amsrefs/cite-xa.pdf
%doc %{_texmfdistdir}/doc/latex/amsrefs/cite-xa.tex
%doc %{_texmfdistdir}/doc/latex/amsrefs/cite-xb.pdf
%doc %{_texmfdistdir}/doc/latex/amsrefs/cite-xb.tex
%doc %{_texmfdistdir}/doc/latex/amsrefs/cite-xh.pdf
%doc %{_texmfdistdir}/doc/latex/amsrefs/cite-xh.tex
%doc %{_texmfdistdir}/doc/latex/amsrefs/cite-xs.pdf
%doc %{_texmfdistdir}/doc/latex/amsrefs/cite-xs.tex
%doc %{_texmfdistdir}/doc/latex/amsrefs/gktest.ltb
%doc %{_texmfdistdir}/doc/latex/amsrefs/ifoption.pdf
%doc %{_texmfdistdir}/doc/latex/amsrefs/jr.bib
%doc %{_texmfdistdir}/doc/latex/amsrefs/mathscinet.pdf
%doc %{_texmfdistdir}/doc/latex/amsrefs/pcatcode.pdf
%doc %{_texmfdistdir}/doc/latex/amsrefs/rkeyval.pdf
%doc %{_texmfdistdir}/doc/latex/amsrefs/textcmds.pdf
#- source
%doc %{_texmfdistdir}/source/latex/amsrefs/00readme.txt
%doc %{_texmfdistdir}/source/latex/amsrefs/amsrdoc.tex
%doc %{_texmfdistdir}/source/latex/amsrefs/amsrefs.dtx
%doc %{_texmfdistdir}/source/latex/amsrefs/amsrefs.ins
%doc %{_texmfdistdir}/source/latex/amsrefs/amsxport.dtx
%doc %{_texmfdistdir}/source/latex/amsrefs/amsxport.ins
%doc %{_texmfdistdir}/source/latex/amsrefs/changes.tex
%doc %{_texmfdistdir}/source/latex/amsrefs/ifoption.dtx
%doc %{_texmfdistdir}/source/latex/amsrefs/ifoption.ins
%doc %{_texmfdistdir}/source/latex/amsrefs/install.txt
%doc %{_texmfdistdir}/source/latex/amsrefs/manifest.txt
%doc %{_texmfdistdir}/source/latex/amsrefs/mathscinet.dtx
%doc %{_texmfdistdir}/source/latex/amsrefs/mathscinet.ins
%doc %{_texmfdistdir}/source/latex/amsrefs/pcatcode.dtx
%doc %{_texmfdistdir}/source/latex/amsrefs/pcatcode.ins
%doc %{_texmfdistdir}/source/latex/amsrefs/rkeyval.dtx
%doc %{_texmfdistdir}/source/latex/amsrefs/rkeyval.ins
%doc %{_texmfdistdir}/source/latex/amsrefs/textcmds.dtx
%doc %{_texmfdistdir}/source/latex/amsrefs/textcmds.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc source %{buildroot}%{_texmfdistdir}