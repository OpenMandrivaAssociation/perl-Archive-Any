%define	module	Archive-Any
%define	name	perl-%{module}
%define version 0.0932
%define release %mkrel 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Single interface to deal with file archives
License:	GPL or Artistic
Group:		Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Archive/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(Test::Warn)
BuildRequires:  perl(Test::Pod::Coverage)
BuildRequires:  perl(Module::Find)
BuildRequires:  perl(File::MMagic)
BuildRequires:  perl(MIME::Types)
BuildRequires:  perl(Archive::Zip)
BuildRequires:  perl(Archive::Tar)
BuildRequires:  perl(IO::Zlib)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module is a single interface for manipulating different archive formats.
Tarballs, zip files, etc.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
%{__rm} -rf %{buildroot}
%{makeinstall_std}

%clean 
%{__rm} -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Archive
%{_mandir}/man3/*



