%include	/usr/lib/rpm/macros.perl
%define		pdir	Convert
%define		pnam	PEM
Summary:	Convert::PEM Perl module - access to ASN.1-encoded PEM files
Summary(pl):	Modu³ Perla Convert::PEM - dostêp do plików PEM kodowanych ASN.1
Name:		perl-Convert-PEM
Version:	0.06
Release:	1
License:	Artistic or GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Convert-ASN1 >= 0.10
BuildRequires:	perl-Crypt-DES_EDE3
BuildRequires:	perl-Digest-MD5
BuildRequires:	rpm-perlprov >= 3.0.3-16
Requires:	perl(Convert::ASN1) >= 0.10
Requires:	perl-Crypt-DES_EDE3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::PEM reads and writes PEM files containing ASN.1-encoded
objects. The files can optionally be encrypted using a symmetric
cipher algorithm, such as 3DES.

%description -l pl
Modu³ Convert::PEM s³u¿y do odczytu i zapisu plików PEM zawieraj±cych
obiekty zakodowane zgodnie z ASN.1. Pliki mog± byæ opcjonalne
zaszyfrowane algorytmem symetrycznym, takim jak na przyk³ad 3DES.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README ToDo
%{perl_sitelib}/Convert/PEM.pm
%{perl_sitelib}/Convert/PEM
%{_mandir}/man3/*
