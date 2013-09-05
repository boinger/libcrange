Name:     libcrange
Version:  1.0.2
Release:  1%{?dist}
Summary:  C version of range

Group:      System Environment/Libraries
License:    GPL
URL:        http://github.com/boinger/libcrange
Source:    %{name}-latest.tar.gz
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: autoconf, automake, apr-devel, bison, flex, libtool, libyaml, libyaml-devel, pcre-devel, perl-devel, sqlite-devel, perl-ExtUtils-Embed
Requires: apr, libyaml, pcre, perl, perl-YAML-Syck, perl-core, perl-libs, sqlite


%description
A library for parsing and generating range expressions.


%prep
%setup -q -n source


%build
aclocal
libtoolize --force
autoheader
automake -a
autoconf
export LDFLAGS="-L%{buildroot}/src/.libs"
%configure --prefix=/usr
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc
%{_bindir}/crange
%{_includedir}/libcrange.h
%{_libdir}/libcrange*


%changelog

* Mon Aug 05 2013 Jeff Vier <jeff@jeffvier.com> - 1.0.2-1
- add Requires/BuildRequires

