#
# Conditional build:
%bcond_without  tests           # do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	MasonX
%define	pnam	Request-HTMLTemplate
Summary:	MasonX::Request::HTMLTemplate - add templates to the Mason Request object
Summary(pl):	MasonX::Request::HTMLTemplate - dodawanie szablonów do obiektu Mason Request
Name:		perl-MasonX-Request-HTMLTemplate
Version:	0.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	f36c65732f9da854cc2cb84a9d8ca9ed
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-Mason
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module tries to add two peculiar functionalities to Mason:
 - easy use of templates;
 - easy building of localized web site;
to produce a framework with all power of Mason but by separating
completely the script language from the graphical interface language.

%description -l pl
Ten modu³ próbuje dodaæ dwie szczególne funkcjonalno¶ci do Masona:
 - ³atwe u¿ywanie szablonów;
 - ³atwe budowanie zlokalizowanych serwisów WWW
aby stworzyæ szkielet z ca³± si³± Masona, ale oddzielaj±c ca³kowicie
jêzyk skryptowy od jêzyka interfejsu graficznego.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/MasonX/*/*.pm
%{perl_vendorlib}/MasonX/Request/HTMLTemplate
%{_mandir}/man3/*
