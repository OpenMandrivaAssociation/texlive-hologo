Name:		texlive-hologo
Version:	61719
Release:	2
Summary:	A collection of logos with bookmark support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/hologo
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hologo.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hologo.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hologo.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines a single command \hologo, whose argument is
the usual case-confused ASCII version of the logo. The command
is bookmark-enabled, so that every logo becomes available in
bookmarks without further work.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/generic/hologo
%{_texmfdistdir}/tex/generic/hologo
%doc %{_texmfdistdir}/doc/generic/hologo

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
