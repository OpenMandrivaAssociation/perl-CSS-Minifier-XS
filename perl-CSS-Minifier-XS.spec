%define upstream_name    CSS-Minifier-XS
%define upstream_version 0.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	3

Summary:    XS based CSS minifier
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CSS/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
'CSS::Minifier::XS' is a CSS "minifier"; its designed to remove
un-necessary whitespace and comments from CSS files, while also *not*
breaking the CSS.

'CSS::Minifier::XS' is similar in function to 'CSS::Minifier', but is
substantially faster as its written in XS and not just pure Perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
