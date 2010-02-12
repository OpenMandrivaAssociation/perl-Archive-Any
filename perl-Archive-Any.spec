%define	upstream_name	 Archive-Any
%define upstream_version 0.0932

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Epoch:      1

Summary:	Single interface to deal with file archives
License:	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Archive/%{upstream_name}-%{upstream_version}.tar.bz2

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
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module is a single interface for manipulating different archive formats.
Tarballs, zip files, etc.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

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
