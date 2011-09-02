Name:           perl-Test-Pod-Coverage
Version:        1.08
Release:        8.1%{?dist}
Summary:        Check for pod coverage in your distribution

Group:          Development/Libraries
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Test-Pod-Coverage/
Source0:        http://www.cpan.org/authors/id/P/PE/PETDANCE/Test-Pod-Coverage-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  perl(Pod::Coverage)
BuildRequires:  perl(Test::Pod)
Requires:       perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%description
Checks for POD coverage in files for your distribution.


%prep
%setup -q -n Test-Pod-Coverage-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes
%{perl_vendorlib}/Test/
%{_mandir}/man3/*.3pm*


%changelog
* Thu Dec 03 2009 Dennis Gregorovic <dgregor@redhat.com> - 1.08-8.1
- Rebuilt for RHEL 6

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.08-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jul 11 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.08-6
- fix license tag

* Wed Feb 27 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.08-5
- Rebuild for perl 5.10 (again)

* Sun Jan 13 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 1.08-4
- rebuild for new perl

* Fri Sep  8 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.08-3
- Rebuild for FC6.

* Sat Feb 18 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.08-2
- Rebuild for FC5 (perl 5.8.8).

* Thu Jan 26 2006 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.08-1
- Update to 1.08.

* Thu May 12 2005 Jose Pedro Oliveira <jpo at di.uminho.pt> - 1.06-3
- Add dist tag.

* Fri Apr  7 2005 Michael Schwendt <mschwendt[AT]users.sf.net> - 1.06-2
- rebuilt

* Thu Jun 24 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.06-1
- Update to 1.06.

* Wed Jun 02 2004 Jose Pedro Oliveira <jpo at di.uminho.pt> - 0:1.04-0.fdr.1
- First build.
