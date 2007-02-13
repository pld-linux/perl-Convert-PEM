%include	/usr/lib/rpm/macros.perl
%define		pdir	Convert
%define		pnam	PEM
Summary:	Convert::PEM Perl module - access to ASN.1-encoded PEM files
Summary(pl.UTF-8):	Moduł Perla Convert::PEM - dostęp do plików PEM kodowanych ASN.1
Name:		perl-Convert-PEM
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d2188dd87446004c8da882b5a1f20412
URL:		http://search.cpan.org/dist/Convert-PEM/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl-Class-ErrorHandler
BuildRequires:	perl-Convert-ASN1 >= 0.10
BuildRequires:	perl-Crypt-DES_EDE3
BuildRequires:	perl-Digest-MD5
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl(Convert::ASN1) >= 0.10
Requires:	perl-Crypt-DES_EDE3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Convert::PEM reads and writes PEM files containing ASN.1-encoded
objects. The files can optionally be encrypted using a symmetric
cipher algorithm, such as 3DES.

%description -l pl.UTF-8
Moduł Convert::PEM służy do odczytu i zapisu plików PEM zawierających
obiekty zakodowane zgodnie z ASN.1. Pliki mogą być opcjonalne
zaszyfrowane algorytmem symetrycznym, takim jak na przykład 3DES.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
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
%{perl_vendorlib}/Convert/PEM.pm
%{perl_vendorlib}/Convert/PEM
%{_mandir}/man3/*
