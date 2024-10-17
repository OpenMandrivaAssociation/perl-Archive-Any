%define	upstream_name	 Archive-Any
%define upstream_version 0.0941

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3
Epoch:		1

Summary:	Single interface to deal with file archives
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Archive/Archive-Any-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::Warn)
BuildRequires:	perl(Test::Pod::Coverage)
BuildRequires:	perl(Module::Find)
BuildRequires:	perl(File::MMagic)
BuildRequires:	perl(MIME::Types)
BuildRequires:	perl(Archive::Zip)
BuildRequires:	perl(Archive::Tar)
BuildRequires:	perl(IO::Zlib)

BuildArch:	noarch

%description
This module is a single interface for manipulating different archive formats.
Tarballs, zip files, etc.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files 
%doc README
%{perl_vendorlib}/Archive
%{_mandir}/man3/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 1:0.93.200-2mdv2011.0
+ Revision: 680474
- mass rebuild

* Fri Feb 12 2010 Jérôme Quelin <jquelin@mandriva.org> 1:0.93.200-1mdv2011.0
+ Revision: 504570
- bump epoch
- rebuild using %%perl_convert_version

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.0932-3mdv2010.0
+ Revision: 430259
- rebuild

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.0932-2mdv2009.0
+ Revision: 268368
- rebuild early 2009.0 package (before pixel changes)

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - update to new version 0.0932

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.093-2mdv2008.1
+ Revision: 131136
- kill re-definition of %%buildroot on Pixel's request


* Mon Nov 27 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.093-2mdv2007.0
+ Revision: 87501
- fix buildrequires
- Import perl-Archive-Any

* Sat Nov 25 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.093-1mdv2007.1
- first mdv release


