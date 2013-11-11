%define upstream_name    CSS-Minifier-XS
%define upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	1

Summary:    XS based CSS minifier
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/CSS/CSS-Minifier-XS-%{upstream_version}.tar.gz

BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl-devel

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
%makeinstall_std

%clean

%files
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.80.0-3
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.80.0-2
+ Revision: 680705
- mass rebuild

* Mon Nov 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 595091
- update to new version 0.08

* Tue Jul 27 2010 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2011.0
+ Revision: 561029
- update to 0.07

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-2mdv2011.0
+ Revision: 555724
- rebuild

* Mon Apr 26 2010 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.1
+ Revision: 539070
- update to 0.05

* Tue Aug 11 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 415033
- update to 0.04

* Sat May 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.30.0-1mdv2010.0
+ Revision: 381301
- import perl-CSS-Minifier-XS


* Sat May 30 2009 cpan2dist 0.03-1mdv
- initial mdv release, generated with cpan2dist


