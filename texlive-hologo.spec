%global tl_name hologo
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.17
Release:	%{tl_revision}.1
Summary:	A collection of logos with bookmark support
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/hologo
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hologo.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hologo.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hologo.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines a single command \hologo, whose argument is the
usual case-confused ASCII version of the logo. The command is bookmark-
enabled, so that every logo becomes available in bookmarks without
further work.

