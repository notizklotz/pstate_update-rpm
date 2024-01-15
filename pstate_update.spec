Name:           pstate_update
Version:        0.1.10
Release:        1%{?dist}
Summary:        Service that keeps AMD PState EPP up-to-date with power-profiles-daemon

License:        GPL-3.0-or-later
URL:            https://github.com/endrebjorsvik/%{name}
Source0:        https://github.com/endrebjorsvik/%{name}/archive/refs/tags/v%{version}.tar.gz

BuildRequires:  cargo systemd-rpm-macros
Requires:       systemd power-profiles-daemon

%description
Service that keeps AMD PState EPP up-to-date with power-profiles-daemon

%prep
%setup -q
sed -i 's\/usr/local/bin\/usr/bin\g' pstate_update.service


%build
cargo build --release


%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 target/release/%{name} %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}
install -m 0644 config.toml %{buildroot}%{_sysconfdir}/%{name}/config.toml
mkdir -p %{buildroot}%{_unitdir}
install -m 0644 %{name}.service %{buildroot}%{_unitdir}/%{name}.service


%files
%{_bindir}/%{name}
%dir %{_sysconfdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}/config.toml
%{_unitdir}/%{name}.service
%doc README.md


%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service


%changelog
* Mon Jan 15 2024 Adrian Gygax <5250484+notizklotz@users.noreply.github.com> - 0.1.10-1
- First version being packaged
