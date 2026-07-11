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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Amsrefs is a LaTeX package for bibliographies that provides an archival
data format similar to the format of BibTeX database files, but adapted
to make direct processing by LaTeX easier. The package can be used
either in conjunction with BibTeX or as a replacement for BibTeX.

