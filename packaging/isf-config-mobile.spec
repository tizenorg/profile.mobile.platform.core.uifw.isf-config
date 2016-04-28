Name:       isf-config-mobile
Summary:    ISF config files for mobile profile
Version:    0.1.0
Release:    1
Group:      Graphics & UI Framework/Input
License:    Apache-2.0
BuildArch:  noarch
Source0:    %{name}-%{version}.tar.gz
Requires(post): coreutils

%description
ISF configuration files for mobile profile

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_sysconfdir}/scim/conf
%__cp etc/scim/conf/* %{buildroot}%{_sysconfdir}/scim/conf

%files
%defattr(-,root,root,-)
/etc/scim/conf/*
%license LICENSE.APLv2
