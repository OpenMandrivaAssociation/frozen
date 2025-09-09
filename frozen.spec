Name: frozen
Version: 1.2.0
Release: 1
Source0: https://github.com/serge-sans-paille/frozen/archive/refs/tags/%{version}.tar.gz
Summary: Header-only, constexpr alternative to gperf for C++14
URL: https://github.com/serge-sans-paille/frozen
License: Apache-2.0
Group: Development/C and C++
BuildSystem: cmake
BuildArch: noarch

%patchlist
frozen-1.2.0-fix-build-with-Werror.patch

%description
Header-only library that provides 0 cost initialization for immutable
containers, fixed-size containers, and various algorithms.

Frozen provides:

immutable (a.k.a. frozen), constexpr-compatible versions of std::set,
std::unordered_set, std::map and std::unordered_map.
fixed-capacity, constinit-compatible versions of std::map and
std::unordered_map with immutable, compile-time selected keys mapped to
mutable values.

0-cost initialization version of std::search for frozen needles using
Boyer-Moore or Knuth-Morris-Pratt algorithms.
The unordered_* containers are guaranteed perfect (a.k.a. no hash collision)
and the extra storage is linear with respect to the number of keys.

Once initialized, the container keys cannot be updated, and in exchange,
lookups are faster. And initialization is free when constexpr or constinit is
used.

%files
%{_includedir}/frozen
%{_datadir}/cmake/frozen
