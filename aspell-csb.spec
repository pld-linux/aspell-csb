Summary:	Kashubian dictionary for aspell
Summary(pl.UTF-8):	Słownik kaszubski dla aspella
Name:		aspell-csb
Version:	0.02
%define	subv	0
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/csb/aspell6-csb-%{version}-%{subv}.tar.bz2
# Source0-md5:	0d4b408076115b7516c68887a563be68
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kashubian dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik kaszubski (lista słów) dla aspella.

%prep
%setup -q -n aspell6-csb-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
